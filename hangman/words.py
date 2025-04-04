animal_names = (
    "abyssinian", "addax", "affenpinscher", "airedale", "akita", "albatross", "aldabra", "anaconda", "angelfish", "ant",
    "antbird", "arapaima", "arctic fox", "armadillo", "asian elephant", "aye-aye", "baboon", "bactrian camel", "badger",
    "banded palm civet", "barasingha", "barracuda", "basilisk", "binturong", "bird", "bison", "black marlin", "black widow", "bongo",
    "bongo cat", "brahman", "burmese", "butterfly fish", "caiman", "cairn terrier", "capybara", "caracal", "cassowary", "catfish",
    "cheetah", "chinchilla", "chow chow", "cicada", "clownfish", "cockatoo", "coyote", "crested gecko", "cuttlefish", "dachshund",
    "dama gazelle", "dingo", "dodo", "dolphin", "dromedary", "duck-billed platypus", "eagle", "echidna", "eel", "elephant seal",
    "emperor penguin", "emu", "ermine", "falcon", "fennec fox", "finch", "firefly", "fish", "flamingo", "flycatcher",
    "flying fish", "fossa", "foxhound", "frog", "gaur", "gazelle", "gecko", "gibbon", "giraffe", "gnat",
    "goanna", "goose", "gopher", "gorilla", "grizzly bear", "guinea pig", "gull", "hedgehog", "hummingbird", "hyrax",
    "ibex", "iguana", "impala", "inchworm", "indri", "iriomote cat", "jackal", "jaguar", "jellyfish", "kakapo",
    "kangaroo rat", "kea", "koi", "komodo dragon", "kookaburra", "kudu", "labrador", "lemur", "liger", "lionfish",
    "llama", "macaroni penguin", "maine coon", "malayan tiger", "manatee", "marmoset", "meerkat", "minke whale", "mole", "mongoose",
    "moose", "mountain goat", "mouse", "narwhal", "numbat", "okapi", "olingo", "opossum", "orangutan", "orca",
    "otterhound", "ostrich", "pangolin", "parakeet", "peccary", "pelican", "penguin", "perch", "pika", "piranha",
    "platypus", "porcupine", "puma", "quokka", "quoll", "raccoon dog", "red fox", "red panda", "reindeer", "rhino",
    "rottweiler", "salamander", "sand dollar", "scarab", "scorpion", "sea lion", "seahorse", "shark", "sheepdog", "shrew",
    "sifaka", "skimmer", "sloth bear", "snapping turtle", "snow leopard", "sparrow", "spider", "squid", "squirrel monkey", "starling",
    "stingray", "stoat", "tamarin", "tapir", "tasmanian devil", "termite", "thorny devil", "tiger", "tortoise", "toucan",
    "tree frog", "turtle dove", "viper", "vulture", "wallaby", "warthog", "wasp", "weasel", "whippet", "wildcat",
    "wolverine", "woodchuck", "wombat", "zebra", "zorse", "zebu", "african grey", "aldabra tortoise", "american bulldog", "american foxhound",
    "anemonefish", "antarctic fur seal", "arctic hare", "asian elephant", "australian cattle dog", "australian shepherd", "banded palm civet", "bearded dragon", "beetle", "binturong",
    "black rhinoceros", "bloodhound", "bongo", "bornean orangutan", "boxer", "burmese python", "calico cat", "carp", "catfish", "cheetah",
    "chinese crested dog", "chow chow", "coyote", "crested penguin", "dachshund", "dama gazelle", "dingo", "dodo", "dolphin", "dromedary camel",
    "eastern bluebird", "eastern grey kangaroo", "echidna", "eurasian lynx", "fennec fox", "firefly", "flatfish", "flying squirrel", "galápagos tortoise", "gharial",
    "golden retriever", "goose", "great dane", "green iguana", "greyhound", "grizzly bear", "guinea fowl", "hummingbird", "ibex", "indigo bunting",
    "irish setter", "jackrabbit", "japanese macaque", "koi fish", "komodo dragon", "kookaburra", "labradoodle", "lynx", "malayan sun bear", "manx",
    "mastiff", "mole", "mongoose", "musk ox", "newfoundland", "okapi", "ocelot", "ostrich", "otter", "panda",
    "parrotfish", "peacock", "pelican", "peregrine falcon", "persian cat", "platypus", "puffin", "quail", "quokka", "ragdoll",
    "red fox", "red panda", "reindeer", "rottweiler", "salamander", "sardine", "scorpion", "sea turtle", "shih tzu", "siberian husky",
    "snowshoe hare", "sphynx cat", "spotted hyena", "squirrel", "tarantula", "tasmanian tiger", "tetra", "tortoise", "tropical fish", "vervet monkey",
    "warthog", "welsh corgi", "whale shark", "wild boar", "wolverine", "yellowfin tuna", "zebra shark", "zebu", "zonkey",
    "alligator", "armadillo", "aardvark", "badger", "bison", "bear", "beaver", "bee", "bison", "boar",
    "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "cheetah", "chicken", "chinchilla", "cobra",
    "cockatoo", "coyote", "crab", "crocodile", "crow", "deer", "dolphin", "donkey", "dove", "duck",
    "eagle", "eel", "elephant", "falcon", "ferret", "fish", "flamingo", "fox", "frog", "gazelle",
    "gecko", "giraffe", "goat", "goldfish", "goose", "gorilla", "hamster", "hedgehog", "hippopotamus", "horse",
    "hummingbird", "hyena", "iguana", "impala", "jaguar", "kangaroo", "koala", "lemur", "leopard", "lion",
    "llama", "lobster", "macaw", "manatee", "meerkat", "mole", "monkey", "moose", "mouse", "octopus",
    "ocelot", "ostrich", "otter", "owl", "panda", "parrot", "peacock", "penguin", "pig", "pigeon",
    "platypus", "porcupine", "quail", "rabbit", "raccoon", "rat", "reindeer", "rhinoceros", "salamander", "salmon",
    "scorpion", "seahorse", "shark", "sheep", "skunk", "sloth", "snake", "squirrel", "starfish", "stoat",
    "swan", "tapir", "tarantula", "tortoise", "toucan", "turtle", "vulture", "wallaby", "warthog", "weasel",
    "whale", "wolf", "wombat", "woodpecker", "zebra", "ant", "bactrian", "barracuda", "bison",
    "bluejay", "booby", "capon", "chimpanzee", "clownfish", "cormorant", "crayfish", "cuttlefish", "dingo", "duckling",
    "emu", "gazelle", "gopher", "guppy", "hamster", "heron", "hornet", "kestrel", "kiwi", "lizard",
    "mongoose", "narwhal", "numbat", "okapi", "opossum", "pika", "quokka", "quoll", "rattlesnake", "redfish",
    "sandpiper", "scorpion", "seahorse", "shrew", "skink", "snail", "snipe", "sperm whale", "tarpon", "tetra",
    "thresher", "toad", "viper", "whelk", "yellowjacket", "zorse", "aye-aye", "bongo", "capuchin", "dhole",
    "eel", "fennec", "galago", "kudu", "manx", "ocelot", "quoll", "red panda", "serval", "tamarin",
    "uakari", "vicuña", "wombat", "xerus", "yak", "zorse", "antbird", "bluebird", "cockroach", "dodo",
    "eider", "flamingo", "gnat", "heron", " ibis", "jay", "kiwi", "loon", "moth", "nighthawk"
)