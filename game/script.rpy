# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yuzu")
define y_unknown = Character("???")
define slime = Character("SG14")
define k = Character("", kind=nvl, color="00008B")
define sc = Character("SUPERCOMPUTER")
define b = Character("???")

# images (sorry)

image bg lab_placeholder = im.Scale("bg/placeholders/lab_hander.jpg", 1500, 1000)
image bg white = im.Scale("bg/placeholders/white background.jpg", 1500, 1000)
image bg computer = im.Scale("bg/placeholders/sittinatcomputer.jpg", 1500, 1000)
image bg empty_desk = im.Scale("bg/placeholders/emptydesk.jpg", 1500, 1000)
image bg tube1 = im.Scale("bg/placeholders/tube1.jpg", 1500, 1000)
image bg tube2 = im.Scale("bg/placeholders/tube2.jpg", 1500, 1000)
image bg tube3 = im.Scale("bg/placeholders/tube3.jpg", 1500, 1000)
image bg tube4 = im.Scale("bg/placeholders/tube4.jpg", 1500, 1000)
image bg wakingup = im.Scale("bg/placeholders/wakingup.jpg", 1500, 1000)
image bg room = im.Scale("bg/placeholders/room.png", 1500, 1000)
image bg plink = im.Scale("bg/placeholders/plink.JPG", 1500, 1000)
image bg general_placeholder = im.Scale("bg/placeholders/catfish.jpg", 1500, 1000)


image slimegirl = "sprites/slimer.jpg"

define secondpause = Pause(1.5)
define slowdissolve = MultipleTransition([False, Pause(2.0), False, Dissolve(5.0),  True])

# screen to block transitions like fadeins from being clicked through. be sure to turn afm off.
screen noclick():
    zorder 1000
    $ preferences.afm_enable = True


# The game starts here.

label start:
label act1scene1:

    show screen noclick
    scene bg lab_placeholder with slowdissolve
    hide screen noclick
    $ preferences.afm_enable = False

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "it's so loud in here{w} my inventions suck{w} i should buy washi tape...{w} gahhh the headache is making my vision go all weird"
    "all these tiny guys floating & mewling. opening eyes for the first time, lined against the wall. i guess they’re sorta rabbits... just with long tails like sleeping kitties. eyes with full pupils and too-big. everything has its own green small glow…"
    "their own glow… bunnies always dissolving and reforming, always almost making themselves..."
    "grrrr… this things so fucking slow"
    play sound "sfx/538149__fupicat__notification.mp3" volume 0.6
    pause(1)
    show bg white

    k "{cps=*0.5}SUBJECT HEAVEN-WORLD REACHED\nOBJECT RETRIEVED\nCONNECTION--------\n//////{w}\n\n\nWAIT{w}\nHOLD ON{/cps}"

    scene bg computer
    nvl clear

    y "ok… where did my checklist go…?"
    y "pass me my checklist. please&thank you."
    "one of the slime girls digs her hand in her chest and passes me a gooped up clipboard."
    "gahhhh their motor skills still SUCK she’s still so slowwwww"
    y "tysm uh… lets see…"
    y "safety lock, check. system backup, check. teleporter fluid yeah there's still some, check…"
    y "hair… um. does my hair look ok?"
    y "i like JUST cut my bangs. they don’t look good til they’ve grown out a little cuz of the texture and I didn’t even use a mirror this time just the back of my glasses so I’m FUCKED…"
    show slimegirl with Dissolve(1.0)
    slime "..."
    hide slimegirl
    y "..."
    play sound "sfx/538149__fupicat__notification.mp3" volume 0.6
    pause(1)

    show bg white
    k "{cps=*0.5}PROGRAM - /////{/cps}"
    pause(1)
    k "\n\n\n\n\n{cps=*0.5}FAILURE, yeah.{w} Sorry.{/cps}"

    scene bg computer
    nvl clear

    y "ok. GAHHH. whatever it’s fine it’s nothing."
    "when i look back at slime girl she stares back so blankly. they’re always mouth breathing. {w}it’s hard to take it seriously…"
    y "guys i’m so nervous"
    y "it’s been so long since i had anyone visit. i don’t even know how to host anymore."
    y "i mean, i can’t remember the last time i talked to anybody aside from you guys. {w}and vista."
    y "do you think they’ll fuck with my set up…?"
    show slimegirl with Dissolve(1.0)
    slime "..."
    "she keeps opening and closing her mouth like a little fish"
    slime ":0 {w=0.4}:o {w=0.4}:0 {w=0.4}:o{w=0.4}"
    hide slimegirl
    y "…this is stupid…"
    y "whatever i’m gonna grab coffee. don’t touch anything, K? (leaves)"
    scene bg empty_desk with Dissolve(1.0)
    window hide dissolve
    pause(2.5)
    play sound "sfx/538149__fupicat__notification.mp3" volume 0.6
    pause(1)

    show bg white
    k "{cps=*0.5}OK WAIT{w=3.0}{/cps}\n\nOk yeah got it one sec."


    scene bg tube1 with Dissolve(2.0)
    pause(1)
    nvl clear
    "bubbles percolate and things start shaking as the floor rocks and shattering noises bounce off the ceiling."
    window hide dissolve
    scene bg tube2 with Dissolve(2.0)
    pause (1)
    scene bg tube3 with Dissolve(2.0)
    pause(1)
    sc "{cps=*0.5}{color=#00008B}SUCCESS :D{/cps}{/color}"
    window hide
    show bg white with Dissolve(3.0)
    # act1 scene 2

    play sound "sfx/whistle.mp3"
    show bg wakingup with Dissolve(3.0)
    pause(1)
    show bg plink
    pause(1)
    "where am i{w}\nwhere was i"
    b "Um. Where am i"
    show bg general_placeholder with Dissolve(2.0)
    b "there was my pond, and i was napping near the pond"
    b "and everything was beautiful"
    b "and light"
    b "and it was like i died…"
    b "and now im alive… and can think"
    window hide
    show bg room with Dissolve(2.0)
    pause(1)
    b "weird"
    "*knock knock*"
    y_unknown "how are you feeeliiingggg?"
    "a girl wearing a lab coat walks in, pushing a cart full of IVs and vials."
    b "wha… (rubbing eyes) who are you"
    y "oh, im sorry. I’m yuzu ..um what’s your name?"
    b "uhh"
    show bg general_placeholder with Dissolve(2.0)
    "name… i dunno my name…"
    "was this how i looked? i dreamed i looked different than this.."
    b "i don’t know. i guess i’m a bird…"
    show bg room with Dissolve(2.0)
    y "oh… well, i can name you"
    y "hmmmm.. what if your name was"
    y "..aerith"
    b "..."
    y "it’s a good name dude i promise. whenever you remember your real name we can change it too"
    b "i’ll be aerith its cool. why’s everything so scrambled ..i feel crazy"
    y "you got teleported"
    show bg general_placeholder with Dissolve(2.0)
    y "here, drink this super teleportation sick medicine i made"
    show bg general_placeholder with Dissolve(2.0)
    b "oh sweet."
    b "are you like, a scientist or something?"
    "the sides are so sticky. either with lemon or honey… or, some icky, lab stuff"
    y "yeah and you’re gonna be my first subject"
    y "if that’s cool with you"
    b "umm yeah its cool. what am i supposed to do?"
    y "mostly experiments and stuff"
    "i take a lil sip."
    b "what kinda experiments, like, cool ones, or painful ones?"
    y "fun ones mostly, the fun kind"
    y "you can pick the first one"
    b "hehe ok"
    b "can we fly?"


    "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
