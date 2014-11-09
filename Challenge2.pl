use Modern::Perl;

package Player;
use Moose;

has 'name' => (
  is => 'rw',
);

has 'gender' => (
  is => 'rw',
);

has 'health' => (
  is => 'rw',
  default => sub { return 100 },
);

has 'score' => (
  is => 'rw',
  default => sub { return 0 },
);

has 'current_room' => (
  is => 'rw',
  isa => 'Room',
);

has 'session' => (
  is => 'rw',
  isa => 'HashRef',
  default => sub { {} },
);

sub move {
  my ($self) = @_;

  my $direction;
  my $question = Question->new(
    player => $self,
    options => {
      North => 'n',
      South => 's',
      East => 'e',
      West => 'w',
      Up => 'u',
      Down => 'd',
    },
    prompt => "Which direction would you like to go? (n)orth, (s)outh, (e)ast, (w)est, (u)p, or (d)own",
    exception => "You can't go that way. (n)orth, (s)outh, (e)ast, (w)est, (u)p, or (d)own",
  );
  while (!$direction) {
    $direction = $question->ask;
    if (!$self->current_room->$direction) {
      if ($direction eq 'u' || $direction eq 'd') {
        say "there aren't any stairs or ladders here.";
      }
      else {
        say "ouch! you ran into a wall!";
      }
      $direction = undef;
    }
  }

  $self->current_room($self->current_room->$direction);
}

package Question;
use Moose;

has 'options' => (
  is => 'rw',
  isa => 'Maybe[HashRef]',
  default => sub {
    return {
      Yes => 'y',
      No => 'n',
    }
  }
);

has 'type' => (
  is => 'ro',
  default => 'Str',
);

has 'prompt' => (
  is => 'rw',
  default => '(y)es or (n)o?',
);

has 'exception' => (
  is => 'rw',
  default => '(y)es or (n)o?',
);

has 'player' => (
  is => 'rw',
  isa => 'Player',
);

sub ask {
  my ($self) = @_;

  print $self->prompt . ": ";
  my $answer;
  while (!$answer) {
    my $input = <>;
    chomp $input;

    exit if $input eq 'q';

    if ($input eq 'i' && $self->player) {
      say "Your current Health is: " . $self->player->health;
      say "Your current Score is: " . $self->player->score;
      $input = undef;
    }
    
    if ($self->type eq 'Num') {
      use Scalar::Util qw/looks_like_number/;
      $input = undef if !looks_like_number($input);
    }
    if ($input && $self->options) {
      foreach (keys %{$self->options}) {
        if ($_ =~ /^$input/i) {
          $answer = $self->options->{$_};
        }
      }
    }
    else {
      $answer = $input;
    }
    print $self->exception . ": " if !$answer;
  }
  return $answer;
}

package Room;
use Moose;

has description => (
  is => 'rw',
);

has session => (
  is => 'rw',
  isa => 'HashRef',
  default => sub { {} },
);

has n => (
  is => 'rw',
  isa => 'Room',
  trigger => sub {
    my ( $self, $n, $old_n ) = @_;
    $n->s($self) if !defined $old_n;
  },
);

has s => (
  is => 'rw',
  isa => 'Room',
  trigger => sub {
    my ( $self, $s, $old_s ) = @_;
    $s->n($self) if !defined $old_s;
  },
);

has w => (
  is => 'rw',
  isa => 'Room',
  trigger => sub {
    my ( $self, $w, $old_w ) = @_;
    $w->e($self) if !defined $old_w;
  },
);

has e => (
  is => 'rw',
  isa => 'Room',
  trigger => sub {
    my ( $self, $e, $old_e ) = @_;
    $e->w($self) if !defined $old_e;
  },
);

has u => (
  is => 'rw',
  isa => 'Room',
  trigger => sub {
    my ( $self, $u, $old_u ) = @_;
    $u->d($self) if !defined $old_u;
  },
);

has d => (
  is => 'rw',
  isa => 'Room',
  trigger => sub {
    my ( $self, $d, $old_d ) = @_;
    $d->u($self) if !defined $old_d;
  },
);

has game => (
  is => 'ro',
  isa => 'CodeRef',
);

package Game;

my $dungeon = Room->new(
  description => "You find yourself in a room. There are doors on all 4 walls.",
  n => Room->new(
    description => "The room you have entered is rather dark. You hear someone breathing in the corner.",
    session => {
      game_tries => 0,
      game_denies => 0,
    },
    game => sub {
      my ($room, $player) = @_;
      $room->session->{game_number} ||= int ((rand)*10) + 1;
      sleep 1;
      say "";
      if ($room->session->{game_denies} > 1) {
        say "Mysterious Person: Go away, this is MY room!";
        return;
      }
      elsif ($room->session->{game_denies} == 1) {
        say "Mysterious Persion: It's you again, ready to play now?";
      }
      elsif ($room->session->{game_tries} > 0) {
        say "You're back! Do you want to play again?";
      }
      else {
        say "Mysterious Person: Hello " . $player->name . "... you want to play a game?";
      }
      my $y_or_n = Question->new( player => $player )->ask;
      if ($y_or_n eq 'y') {
        my $guess = Question->new(
          player => $player,
          options => undef,
          type => 'Num',
          prompt => "Mysterious Person: I'm thinking of a number between 1 and 10, can you guess what it is?",
          exception => "Huh?",
        )->ask;
        if ($guess == $room->session->{game_number}) {
          sleep 1;
          say "Mysterious Person: You got it!";
          $player->score($player->score + 10);
          $room->session->{game_number} = undef;
        }
        else {
          sleep 1;
          say "Mysterious Person: Nope.";
          if ($guess < $room->session->{game_number}) {
            say "Mysterious Person: Maybe try a little higher next time...";
          }
          else {
            say "Mysterious Person: Maybe try a little lower next time...";
          }
        }
        $room->session->{game_tries}++;
      }
      else {
        sleep 1;
        say "";
        if ($room->session->{game_denies} > 0) {
          say "You: still no.";
          sleep 1;
          say "";
          say "Mysterious Person: you're really going to regret this now!";
        }
        else {
          say "You: I don't think so... but thanks anyways...";
          sleep 1;
          say "";
          say "Mysterious Person: you're going to regret this!";
        }
        $room->session->{game_denies}++;
      }
    },
  ),
  s => Room->new(
    description => "The room you have entered is lit by a stream of light coming through a skylight in the ceiling.",
  ),
  e => Room->new(
    description => "You have entered what appears to be a child's room.",
  ),
  w => Room->new(
    description => "You are in the bathroom. Gotta pee?",
  ),
);

say "An adventure awaits!";
say "";

my $player = Player->new(
  current_room => $dungeon,
);

say "Enter 'q' to quit";
say "Enter 'i' for information";
say "";

$player->name( Question->new( player => $player, options => undef, prompt => "What is your name?", exception => "What is your name?" )->ask );

$player->gender( Question->new(
  player => $player,
  options => { male => 'male', female => 'female' },
  prompt => "What is your gender? (m)ale or (f)emale",
  exception => "What is your gender? (m)ale or f(emale)",
)->ask );

say "";
say "Welcome to the Baerg Mansion, " . $player->name . "!";
say "";


while ($player->health > 0) {
  sleep 1;
  say "";
  say $player->current_room->description;
  if (defined $player->current_room->game) {
    $player->current_room->game->($player->current_room, $player);
  }
  say '';
  $player->move();
}

1;

