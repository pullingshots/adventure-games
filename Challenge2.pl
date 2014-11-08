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
);

has 'current_room' => (
  is => 'rw',
  isa => 'Room',
);

sub move {
  my ($self) = @_;
  print "Which direction would you like to go? (n,s,e,w): ";
  my $direction;
  while (!$direction) {
    $direction = <>;
    chomp $direction;
    if ($self->current_room->can($direction) && $self->current_room->$direction) {
    }
    else {
      $direction = undef;
      print "You ran into a wall, try again (n,s,e,w): ";
    }
  }
  $self->current_room($self->current_room->$direction);
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

has game => (
  is => 'ro',
  isa => 'CodeRef',
);

package Game;

my $dungeon = Room->new(
  description => "You are in a dark cell. There are doors on all 4 walls.",
  n => Room->new(
    description => "You are surrounded by cobwebs.",
    game => sub { my ($player) = @_; say "Hello " . $player->name . "... you want to play a game?"; },
  ),
  s => Room->new(
    description => "You see a stream of light coming through a barred window above you."
  ),
);

say "Welcome to my game!";
print "What is your name? ";
my $name = <>;
chomp $name;
print "What is your gender? ";
my $gender = <>;
chomp $gender;
my $player = Player->new(
  name => $name,
  gender => $gender,
  health => 100,
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

