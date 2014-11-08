use Modern::Perl;

package Player;
use Moose;

has 'name' => (
  is => 'ro',
);

has 'gender' => (
  is => 'ro',
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

sub move {
  my ($self) = @_;

  my $direction;
  my $question = Question->new(
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

has 'prompt' => (
  is => 'rw',
  default => 'Yes or No?',
);

has 'exception' => (
  is => 'rw',
  default => 'That is an invalid response, Yes or No?',
);

sub ask {
  my ($self) = @_;

  print $self->prompt . ": ";
  my $answer;
  while (!$answer) {
    my $input = <>;
    chomp $input;
    if ($input && $self->options) {
      exit if $input eq 'q';
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
  is => 'ro',
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
  description => "You find yourself in room. There are doors on all 4 walls.",
  n => Room->new(
    description => "The room you have entered is rather dark. You hear someone breathing in the corner.",
    game => sub {
      my ($player) = @_;
      say "Hello " . $player->name . "... you want to play a game?";
      
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
my $name = Question->new( options => undef, prompt => "What is your name?", exception => "What is your name?" )->ask;
my $gender = Question->new(
  options => { male => 'male', female => 'female' },
  prompt => "What is your gender? (m)ale or f(emale)",
  exception => "What is your gender? (m)ale or f(emale)",
)->ask;
my $player = Player->new(
  name => $name,
  gender => $gender,
  current_room => $dungeon,
);

say "Your name is " . $player->name;
while ($player->health > 0) {
  say $player->current_room->description;
  if (defined $player->current_room->game) {
    $player->current_room->game->($player);
  }
  $player->move();
}

1;

