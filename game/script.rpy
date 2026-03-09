# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Frankie", color="#F1E05A")   # POV
define b = Character("Brenda",  color="#F97A5A")   # Brenda
# You can define more later:
define m = Character("Mick", color="#A0E7E5")
define j = Character("Joanie", color="#C9A3FF")
define a = Character("Andy", color="#7FC8FF")
define d = Character("Doris", color="#A6FFB3")
define a = Character("Andy", color="#7FC8FF")
define r = Character("Rowan", color="#D0D0D0")
define h = Character("Harry",  color="#A0E7E5")
define n = Character("Sister Nancy", color="#FFFFFF")
define k = Character("Kirsty", color="#F2B6FF")




define audio.act1 = "audio/music/Act1_Loop.ogg"
define audio.act2 = "audio/music/Act2_Loop.ogg"
define audio.act3 = "audio/music/Act3_Loop.ogg"
define audio.act4 = "audio/music/Act4_Loop.ogg"
define audio.moral = "audio/music/MoralChoice_Loop.ogg"

# ---------- SFX DEFINITIONS ----------

define audio.sfx_button5      = "audio/sfx/Button5.ogg"
define audio.sfx_button6      = "audio/sfx/Button6.ogg"
define audio.sfx_button7      = "audio/sfx/Button7.ogg"
define audio.sfx_button8      = "audio/sfx/Button8.ogg"

define audio.sfx_bomb         = "audio/sfx/SFX_Bomb.ogg"
define audio.sfx_gunshot      = "audio/sfx/SFX_Gunshot.ogg"
define audio.sfx_kickchair    = "audio/sfx/SFX_KickChair.ogg"
define audio.sfx_kickdog      = "audio/sfx/SFX_KickDog.ogg"
define audio.sfx_opendoor     = "audio/sfx/SFX_OpenDoor.ogg"
define audio.sfx_lever        = "audio/sfx/SFX_PushLever.ogg"
define audio.sfx_sandwich     = "audio/sfx/SFX_TakeSandwich.ogg"
define audio.sfx_coin         = "audio/sfx/SFX_ThrowCoin.ogg"
define audio.sfx_trip         = "audio/sfx/SFX_TripTeenager.ogg"



# ---------- VARIABLES ----------

default choice_timeout = None

default morality   = 15      # Twine starts at 15
default popularity = 0

default ate_sausage    = False
default stole_from_mick = False
default kicked_the_dog = False
default moira_dead       = False
default kids_dead        = False
default feros_dead       = False
default explosion        = False
default timed_out_harry  = False
default harry_dead       = False
# ---------- ACT IV DEFAULTS ----------
default checked_icechests   = False
default checked_stove       = False
default checked_auditorium  = False
default indecisive          = False

# You already have: stole_from_andy, ate_sausage, stole_from_mick, kicked_the_dog, morality, popularity
# But Twine also tracks these (add if you haven't already):


# You can define later:
# image bg foyer        = "images/BG_Foyer.png"
# image dog_front       = "images/Dog_Front.png"

image bg town_long_shot = "images/BG_TownLongShot.png"
image bg street_view = "images/BG_StreetView.png"
image brenda_sandwich = "images/Brenda_Sandwich.png"
image bg Dilemma2_PreDog = "images/Dilemma2_PreDog.png"
image bg Dilemma2_PostDogKick = "images/Dilemma2_PostDogKick.png"
image mick_neutral = "images/Mick_Neutral.png"
image bg Dilemma1_PreMick = "images/Dilemma1_PreMick.png"
image bg Dilemma1_PostMick = "images/Dilemma1_PostMick.png"

# ---------- ACT II BACKGROUNDS ----------

# Copy these from the Unity repo into game/images/ or game/images/Dilemmas/

image bg foyer             = "images/BG_Foyer.png"
image bg lolly_counter     = "images/BG_LollyCounter.png"
image bg auditorium        = "images/BG_Auditorium.png"
image bg auditorium_empty  = "images/BG_Auditorium_Empty.png"

# Coin toss and Andy wallet dilemmas
image bg Dilemma2_5_CoinFlip = "images/Dilemma2.5_CoinFlip.png"
image bg Dilemma3_PreAndy    = "images/Dilemma3_PreAndy.png"
image bg Dilemma3_PostAndy   = "images/Dilemma3_PostAndy.png"


default stole_from_andy = False


# ==========================================================
# CLEAN IMAGE DEFINITIONS
# All files are in: game/images/
# No subfolders.
# ==========================================================

# ------------------------------
# BACKGROUNDS (Twine BG_*)
# ------------------------------

image bg BG_TownLongShot           = "images/BG_TownLongShot.png"
image bg BG_StreetView             = "images/BG_StreetView.png"
image bg BG_StreetView_Fire        = "images/BG_StreetView_Fire.png"

image bg BG_Foyer                  = "images/BG_Foyer.png"
image bg BG_FoyerNew               = "images/BG_FoyerNew.png"

image bg BG_Kitchen                = "images/BG_Kitchen.png"
image bg BG_LollyCounter           = "images/BG_LollyCounter.png"

image bg BG_Auditorium             = "images/BG_Auditorium.png"
image bg BG_Auditorium_Empty       = "images/BG_Auditorium_Empty.png"

image bg BG_Corridor               = "images/BG_Corridor.png"
image bg BG_Hallway                = "images/BG_Hallway.png"

image bg BG_ProjectionRoom         = "images/BG_ProjectionRoom.png"
image bg BG_ProjectionRoom_MrFeros = "images/BG_ProjectionRoom_MrFeros.png"

image bg BG_Outro                  = "images/BG_Outro.png"
image bg BG_Outro_Alternative      = "images/BG_Outro_Alternative.png"


# ------------------------------
# DILEMMAS (also backgrounds)
# ------------------------------

image bg Dilemma1_PreMick          = "images/Dilemma1_PreMick.png"
image bg Dilemma1_PostMick         = "images/Dilemma1_PostMick.png"

image bg Dilemma2_PreDog           = "images/Dilemma2_PreDog.png"
image bg Dilemma2_PostDogKick      = "images/Dilemma2_PostDogKick.png"

image bg Dilemma2_5_CoinFlip       = "images/Dilemma2.5_CoinFlip.png"

image bg Dilemma3_PreAndy          = "images/Dilemma3_PreAndy.png"
image bg Dilemma3_PostAndy         = "images/Dilemma3_PostAndy.png"

image bg Dilemma4a_Lever_PreMoira  = "images/Dilemma4a_Lever_PreMoira.png"
image bg Dilemma4a_Lever_PostMoira = "images/Dilemma4a_Lever_PostMoira.png"

image bg Dilemma4b_Lever_PreABC    = "images/Dilemma4b_Lever_PreABC.png"
image bg Dilemma4b_Lever_PostABC   = "images/Dilemma4b_Lever_PostABC.png"

image bg Dilemma5a_PreFeros        = "images/Dilemma5a_PreFeros.png"
image bg Dilemma5a_PostFeros       = "images/Dilemma5a_PostFeros.png"
image bg Dilemma5b_PostExplosion   = "images/Dilemma5b_PostExplosion.png"

image bg Dilemma6_PreHarry         = "images/Dilemma6_PreHarry.png"
image bg Dilemma6a_PostHarryAlive  = "images/Dilemma6a_PostHarryAlive.png"
image bg Dilemma6b_PostHarryDead   = "images/Dilemma6b_PostHarryDead.png"


# ------------------------------
# DETAIL OVERLAYS (Twine Detail_*)
# ------------------------------

image Detail_Dog                      = "images/Detail_Dog.png"

image Detail_Door_Open                = "images/Detail_Door_Open.png"
image Detail_Door_Closed              = "images/Detail_Door_Closed.png"

image Detail_Office                   = "images/Detail_Office.png"

image Detail_Rowan                    = "images/Detail_Rowan.png"
image Detail_ProjectionRoom_Rowan     = "images/Detail_ProjectionRoom_Rowan.png"
image Detail_ProjectionRoom_Feros     = "images/Detail_ProjectionRoom_Feros.png"

image Detail_Kirsty                   = "images/Detail_Kirsty.png"
image Detail_ThreeWounded             = "images/Detail_ThreeWounded.png"


# ------------------------------
# CHARACTER SPRITES
# ------------------------------

image Joanie_Neutral        = "images/Joanie_Neutral.png"
image Joanie_Nauseous       = "images/Joanie_Nauseous.png"
image Joanie_Unimpressed    = "images/Joanie_Unimpressed.png"

image Brenda_Sandwich       = "images/Brenda_Sandwich.png"
image Brenda_Glass          = "images/Brenda_Glass.png"

image Andy_Neutral          = "images/Andy_Neutral.png"

image Doris_Friendly        = "images/Doris_Friendly.png"
image Doris_Singing         = "images/Doris_Singing.png"

image Mick_Neutral          = "images/Mick_Neutral.png"
image Mick_Concerned        = "images/Mick_Concerned.png"

image Nancy_Worried         = "images/Nancy_Worried.png"
image Nancy_Praying         = "images/Nancy_Praying.png"

image Rowan_Stoic           = "images/Rowan_Stoic.png"
image Rowan_Afraid          = "images/Rowan_Afraid.png"

image Harry_Neutral_Gun        = "images/Harry_Neutral_Gun.png"
image Harry_Gloating_Gun       = "images/Harry_Gloating_Gun.png"
image Harry_Gloating_GunRaised = "images/Harry_Gloating_GunRaised.png"
image Harry_Angry_GunRaised    = "images/Harry_Angry_GunRaised.png"

image ABC_Happy             = "images/ABC_Happy.png"
image ABC_Neutral           = "images/ABC_Neutral.png"


# ------------------------------
# GROUP SPRITES
# ------------------------------

image GROUP_AndyKirsty               = "images/GROUP_AndyKirsty.png"
image GROUP_AndyKirstyMoira          = "images/GROUP_AndyKirstyMoira.png"
image GROUP_Andy_KirstyEmbarrassed   = "images/GROUP_Andy_KirstyEmbarrassed.png"

image GROUP_NancyABC                 = "images/GROUP_NancyABC.png"
image GROUP_JoanieRowan              = "images/GROUP_JoanieRowan.png"

image GROUP_HarryGloating_AndySobbing   = "images/GROUP_HarryGloating_AndySobbing.png"
image GROUP_HarryGloating_AndyTerrified = "images/GROUP_HarryGloating_AndyTerrified.png"



# ---------- ACT II CHARACTER / GROUP SPRITES ----------

image joanie_neutral          = "images/Joanie_Neutral.png"
image joanie_nauseous         = "images/Joanie_Nauseous.png"
image joanie_unimpressed      = "images/Joanie_Unimpressed.png"

image group_andykirstymoira   = "images/GROUP_AndyKirstyMoira.png"
image group_andy_kirstyemb    = "images/GROUP_Andy_KirstyEmbarrassed.png"

image group_nancy_abc         = "images/GROUP_NancyABC.png"
image abc_happy               = "images/ABC_Happy.png"

image doris_friendly          = "images/Doris_Friendly.png"

image andy_neutral            = "images/Andy_Neutral.png"

#NEWONES

image bg BG_TownLongShot       = "images/BG_TownLongShot.png"
image bg BG_StreetView         = "images/BG_StreetView.png"
image bg BG_StreetView_Fire    = "images/BG_StreetView_Fire.png"

image bg BG_Foyer              = "images/BG_Foyer.png"
image bg BG_LollyCounter       = "images/BG_LollyCounter.png"
image bg BG_Auditorium         = "images/BG_Auditorium.png"
image bg BG_Auditorium_Empty   = "images/BG_Auditorium_Empty.png"
image bg BG_Hallway            = "images/BG_Hallway.png"
image bg BG_Corridor           = "images/BG_Corridor.png"

image bg BG_ProjectionRoom         = "images/BG_ProjectionRoom.png"
image bg BG_ProjectionRoom_MrFeros = "images/BG_ProjectionRoom_MrFeros.png"

# --- Dilemmas (backgrounds) ---
image bg Dilemma1_PreMick      = "images/Dilemma1_PreMick.png"
image bg Dilemma1_PostMick     = "images/Dilemma1_PostMick.png"

image bg Dilemma2_PreDog       = "images/Dilemma2_PreDog.png"
image bg Dilemma2_PostDogKick  = "images/Dilemma2_PostDogKick.png"

image bg Dilemma2_5_CoinFlip   = "images/Dilemma2.5_CoinFlip.png"

image bg Dilemma3_PreAndy      = "images/Dilemma3_PreAndy.png"
image bg Dilemma3_PostAndy     = "images/Dilemma3_PostAndy.png"

# (Later acts — safe to define now if you already have them)
image bg Dilemma4a_Lever_PreMoira  = "images/Dilemma4a_Lever_PreMoira.png"
image bg Dilemma4a_Lever_PostMoira = "images/Dilemma4a_Lever_PostMoira.png"
image bg Dilemma4b_Lever_PreABC    = "images/Dilemma4b_Lever_PreABC.png"
image bg Dilemma4b_Lever_PostABC   = "images/Dilemma4b_Lever_PostABC.png"
image bg Dilemma5a_PreFeros        = "images/Dilemma5a_PreFeros.png"
image bg Dilemma5a_PostFeros       = "images/Dilemma5a_PostFeros.png"
image bg Dilemma5b_PostExplosion   = "images/Dilemma5b_PostExplosion.png"
image bg Dilemma6_PreHarry         = "images/Dilemma6_PreHarry.png"
image bg Dilemma6a_PostHarryAlive  = "images/Dilemma6a_PostHarryAlive.png"
image bg Dilemma6b_PostHarryDead   = "images/Dilemma6b_PostHarryDead.png"

# --- Details / overlays ---
image Detail_Door_Open            = "images/Detail_Door_Open.png"
image Detail_Door_Closed          = "images/Detail_Door_Closed.png"
image Detail_Office               = "images/Detail_Office.png"
image Detail_Rowan                = "images/Detail_Rowan.png"
image Detail_ProjectionRoom_Rowan = "images/Detail_ProjectionRoom_Rowan.png"
image Detail_ProjectionRoom_Feros = "images/Detail_ProjectionRoom_Feros.png"
image Detail_Dog                  = "images/Detail_Dog.png"
image Detail_Kirsty               = "images/Detail_Kirsty.png"
image Detail_ThreeWounded         = "images/Detail_ThreeWounded.png"

# --- Sprites (Twine-style) ---
image Brenda_Sandwich     = "images/Brenda_Sandwich.png"
image Joanie_Neutral      = "images/Joanie_Neutral.png"
image Joanie_Nauseous     = "images/Joanie_Nauseous.png"
image Joanie_Unimpressed  = "images/Joanie_Unimpressed.png"
image Doris_Friendly      = "images/Doris_Friendly.png"
image Andy_Neutral        = "images/Andy_Neutral.png"
image ABC_Happy           = "images/ABC_Happy.png"
image ABC_Neutral         = "images/ABC_Neutral.png"
image Rowan_Afraid        = "images/Rowan_Afraid.png"

# --- Groups ---
image GROUP_AndyKirstyMoira        = "images/GROUP_AndyKirstyMoira.png"
image GROUP_Andy_KirstyEmbarrassed = "images/GROUP_Andy_KirstyEmbarrassed.png"
image GROUP_NancyABC               = "images/GROUP_NancyABC.png"
image GROUP_JoanieRowan            = "images/GROUP_JoanieRowan.png"

default participant_id = ""

transform brenda_right_small:
    zoom 0.7
    xalign 0.9
    yalign 1.0

label start:
    
    $ participant_id = renpy.input("Please enter your participant number:", length=20)
    $ participant_id = participant_id.strip()

    while not participant_id.isdigit():
        "Please enter numbers only."
        $ participant_id = renpy.input("Please enter your participant number:", length=20)
        $ participant_id = participant_id.strip()

    $ log_event("participant_entered", entered_id=participant_id)

    "Thank you."

    # your game starts here
    jump p_1_1_intro


# ==========================================================
# ACT I – Faithful + unimportant choices + REAL 30s timeouts
# Replace your whole Act I with this block.
# ==========================================================

label p_1_1_intro:
    play music audio.act1 fadein 1.0
    scene bg town_long_shot
    with fade

    f "This town is called Mayhem."
    f "Ten miles from the railway, a few hundred from Sydney."
    f "Most people wouldn’t look twice at it."
    f "But this town has history now."
    f "And whether or not I like it, I’m a big part of that history."

    "This is what happened, as best as I can tell it."

    "A few months back, before the fire and the headlines, I was just the Orpheum’s usher."
    "I sold popcorn, tore tickets, and shone my torch to show people to their seats."
    "People in town knew me because I worked for them — babysitting, housework, mowing Mrs Costa’s lawn."

    "All that work was for one thing: to save enough to leave Mayhem for Sydney."
    "Someone reckoned they’d seen Mum in Manly."
    "She’d left years ago, promising to come back soon."
    "It wasn’t much to go on, but it was something. So I was saving hard."
    "Since my mother disappeared, the people at the Orpheum have been the only family I have and I care about them. Mr. Feros, especially, has always taken care of me and looked out for me."

    # Reset core flags like Twine does
    $ ate_sausage      = False
    $ stole_from_mick  = False
    $ kicked_the_dog   = False
    $ stole_from_andy  = False
    $ morality         = 15
    $ popularity       = 0
    $ choice_timeout   = None

    

    jump p_1_3_regret


label p_1_3_regret:
    "It’s the end of summer now. The deaths were months ago, but I’m still here."
    "Still remembering. Still wondering what else I could have done."

    menu:
        "Sometimes I think the regret is useless.":
            f "Regret’s like a slap across the face before the next time."
            f "It doesn’t change what happened. It just stings."
            jump p_1_4_hot_day

        "Sometimes the regret helps.":
            f "Regret’s like a slap across the face before the next time."
            f "It hurts, but it keeps me from pretending none of it was my fault."
            jump p_1_4_hot_day


label p_1_4_hot_day:
    scene bg town_long_shot
    with fade

    "On the day of the fire, it was hot. The kind of heat that sticks to your skin."
    "Hot days were good for business. Everyone wanted the fans and the cool dark of the Orpheum."
    "I headed out early for work, just like any other day."

    jump p_1_5_passes_pub


# ==========================================================
# 1.5 Passes pub - Sees Brenda  (unimportant choice restored)
# ==========================================================

label p_1_5_passes_pub:
    scene bg street_view
    show Brenda_Glass at brenda_right_small
    with fade

    "It was a fifteen minute walk from my boarding house to the Orpheum."
    "Being a Sunday morning, the town centre was quiet."
    "Passing by the pub, I smelt stale beer from the night before."
    "I waved to Brenda, who was inside polishing glasses."
    hide Brenda_Glass

    menu:
        "Morning Brenda!":
            jump p_1_5_1_greets_brenda
        "I kept walking.":
            jump p_1_5_2_brenda_calls


label p_1_5_1_greets_brenda:
    show brenda_sandwich at brenda_right_small
    with dissolve

    b "Morning Frankie."
    b "What's showing today?"
    f "Great line-up — Soup’s On, then The Third Man."
    b "Got time for a sausage sandwich?"

    jump p_1_choice_1_sausage


label p_1_5_2_brenda_calls:
    show brenda_sandwich at brenda_right_small
    with dissolve

    b "Want a bite of breakfast? Sausage sandwich?"

    jump p_1_choice_1_sausage


# ==========================================================
# CHOICE 1 - Sausage (TIMED 30s)
# ==========================================================

label p_1_choice_1_sausage:
    "Free tucker was tempting."

    $ choice_timeout = "p_1_5_6_timed_out_walk_away"

    menu:
        "Eat the snag.":
            $ ate_sausage = True
            $ popularity = 88
            hide brenda_sandwich
            with dissolve
            jump p_1_5_4_eat_sausage

        "Decline the offer.":
            $ popularity = 12
            hide brenda_sandwich
            with dissolve
            jump p_1_5_5_decline_sausage


label p_1_5_4_eat_sausage:
    play sound audio.sfx_sandwich
    $ choice_timeout = None
    "Brenda handed me a thick sandwich with fried onion, sauce and a snag."
    "Delicious."
    "I ate it quickly at the bar, then left."
    jump p_1_6_sees_old_mick


label p_1_5_5_decline_sausage:
    $ choice_timeout = None
    f "Thanks, Brenda, but not today."
    "I waved and kept walking."
    jump p_1_6_sees_old_mick


label p_1_5_6_timed_out_walk_away:
    $ choice_timeout = None
    b "Off you go then, if you can't make up your mind."
    "She went back to polishing the glasses."
    hide brenda_sandwich
    with dissolve
    jump p_1_6_sees_old_mick


# ==========================================================
# 1.6 Sees old Mick (unimportant beat restored: “second look”)
# ==========================================================

label p_1_6_sees_old_mick:
    scene black
    show bg Dilemma1_PreMick
    with fade

    "I continued walking, and just past the pub saw old Mick, the stockman, asleep in the shade."
    "This wasn't the first time I'd seen him sleeping it off."
    "He’d come into town every few months when he was finished droving to catch up with family."

    menu:
        "I took a second look.":
            jump p_1_6_1_old_micks_cash


label p_1_6_1_old_micks_cash:
    "Holly moly, that was a lot of money."
    "A bunch of loose notes had fallen from Mick's pocket."
    "Anyone at all could take it."
    "No one would ever know."

    f "Mick… old fella, you asleep?"
    "He didn't stir."

    jump p_1_choice_2_steal_from_mick


# ==========================================================
# CHOICE 2 - Steal from Mick (TIMED 30s)
# ==========================================================

label p_1_choice_2_steal_from_mick:
    "All I had to do was pick the pound notes up, slip them into my pocket and keep walking."
    "And I'd be that much closer to finding my mum."

    $ choice_timeout = "p_1_7_3_timed_out_mick"

    menu:
        "Leave the money.":
            $ stole_from_mick = False
            $ popularity = 86
            $ morality += 1
            jump p_1_7_2_doesnt_steal_from_mick

        "Take the money.":
            $ stole_from_mick = True
            $ popularity = 14
            $ morality -= 1
            jump p_1_7_1_steal_from_mick


label p_1_7_1_steal_from_mick:
    $ choice_timeout = None
    show bg Dilemma1_PostMick
    "In a flash the notes were in my hand."
    "Ten pounds."
    jump p_1_8_smells_smoke


label p_1_7_2_doesnt_steal_from_mick:
    $ choice_timeout = None
    "I left the money where it was."
    jump p_1_8_smells_smoke


label p_1_7_3_timed_out_mick:
    $ choice_timeout = None
    "'Haven't you ever seen a bloke take a kip before?'"
    f "Sorry Mick."
    jump p_1_8_smells_smoke


# ==========================================================
# 1.8 smells smoke
# ==========================================================

label p_1_8_smells_smoke:
    "Walking on, I caught a whiff of ash."
    "A spiral of smoke was spreading a few miles west out of town."
    "My boss Mr Feros had a farm out that way."

    jump p_1_8_1_sees_dog


# ==========================================================
# 1.8.1 Sees Dog (unimportant beat restored: “Come on, take a walk!”)
# ==========================================================

label p_1_8_1_sees_dog:
    scene black
    show bg Dilemma2_PreDog
    with fade

    "By the time I reached the Orpheum I was hot, my hair pasted to my neck."
    "Strangely, there was a dog lying out the front under the movie posters, in the shade of the awning."
    "It wasn't a local dog. It was ugly with mange."

    menu:
        "Come on, take a walk!":
            jump p_1_8_2_shoo_the_dog


label p_1_8_2_shoo_the_dog:
    f "Hey!"
    "An ear twitched in response."
    f "Hey, Doggie, move!"

    jump p_1_choice_3_kick_the_dog


# ==========================================================
# CHOICE 3 - Kick the dog (TIMED 30s)
# ==========================================================

label p_1_choice_3_kick_the_dog:
    "It just lay there."
    "Should I kick it? Then it would run off."
    "Or leave it be?"

    $ choice_timeout = "p_1_8_6_timed_out_dog"

    menu:
        "Don't kick the dog.":
            $ kicked_the_dog = False
            $ popularity = 90
            $ morality += 1
            jump p_1_8_4_leave_dog

        "Kick the dog.":
            $ kicked_the_dog = True
            $ popularity = 10
            $ morality -= 1
            jump p_1_8_5_kick_dog


label p_1_8_4_leave_dog:
    $ choice_timeout = None
    "The dog just lay there, its yellow eyes calmly following my movements."
    jump p_1_end_enter_orpheum


label p_1_8_5_kick_dog:
    play sound audio.sfx_kickdog
    $ choice_timeout = None
    scene black
    show bg Dilemma2_PostDogKick
    with fade
    "I gave it a kick."
    "With an aggrieved yelp, it rose and walked a few feet away, then lay down again."
    jump p_1_end_enter_orpheum


label p_1_8_6_timed_out_dog:
    $ choice_timeout = None
    "Suddenly the dog lunged at me."
    "I stepped back quickly, almost falling off the veranda steps."
    "It snarled a little and stood watching me."
    jump p_1_end_enter_orpheum


# ==========================================================
# End Act I → Act II
# ==========================================================

label p_1_end_enter_orpheum:
    $ choice_timeout = None

    "I nervously unlocked the Orpheum’s front door."
    "Inside, it’ll be cool, dark, and familiar."
    "Outside, somewhere to the west, the smoke creeps closer."

    jump p_2_0_orpheum_start


# ==========================================================
# ACT II – ORPHEUM INTERIOR (Twine-faithful, includes missing beats)
# Covers: 2.0 → 2.12 (up to jump p_3_0_fire_start)
# ==========================================================

label p_2_0_orpheum_start:
    play music audio.act2 fadein 1.0
    scene bg foyer
    with fade

    "The Orpheum felt like a maze if you didn’t know it: foyer, ticket booth, kitchen, stairwell up to Rowan’s projection room, and the long corridor to the auditorium doors."
    "I knew every corner. I’d been working here long enough to walk it blind."

    jump p_2_1_flyers


label p_2_1_flyers:
    scene bg auditorium_empty
    with fade

    "I started my usual routine: checking the downstairs seats and laying out the new program flyers."
    "Front row for the kids from the orphanage and the mission. Back rows for the show-offs and troublemakers."

    "I was partway down the aisle when I heard the front door open in the foyer."

    jump p_2_2_everyone_late


label p_2_2_everyone_late:
    scene bg foyer
    with fade

    "It was later than it should’ve been."
    "Mr Feros wasn’t here yet, and Joanie was juggling the ticket booth and the sweets."

    show joanie_neutral at right
    with dissolve

    j "Hot one, isn’t it?"
    f "Yeah."
    j "Where’s the boss?"
    f "Haven’t seen him."

    "Joanie gave me a harried smile from behind the counter, coins and tickets piled around her elbows."

    hide joanie_neutral
    with dissolve

    jump p_2_2_1_doing_everything


label p_2_2_1_doing_everything:
    scene bg BG_Kitchen
    with fade

    "Which meant I was doing everything else: sweeping, flyers, fans, lights, doors."
    "I shoved fresh popcorn into the machine and listened to it pop and hiss."

    "For a second, I thought I heard my name."

    menu:
        "“Mr Feros?”":
            "No answer."
            jump p_2_3_hears_a_creak
        "I shook it off and kept working.":
            jump p_2_3_hears_a_creak


label p_2_3_hears_a_creak:
    scene bg BG_Foyer
    with fade

    "A creak came from upstairs. A footstep."
    "I looked up the stairwell toward the projection room."

    menu:
        "“Morning, Mr Feros!”":
            "No answer."
            jump p_2_3_people_lining_up
        "I waited, listening.":
            "Nothing."
            jump p_2_3_people_lining_up


label p_2_3_people_lining_up:
    scene bg BG_FoyerNew
    with fade

    "Five minutes to Doors Open."
    "Outside, people were lining up."

    "Mayhem was a small but vocal town that loved its movies."
    "We prided ourselves on punctuality. Doors Open meant doors open."

    jump p_2_4_about_bloody_time


label p_2_4_about_bloody_time:
    scene bg BG_FoyerNew
    with fade

    show GROUP_JoanieRowan at right
    with dissolve

    "At last, Joanie and Rowan arrived in a huff."

    f "About bloody time."
    r "No need for swearing."

    "Rowan stomped upstairs, annoyed."

    j "Oooh."
    f "Oooh."

    hide GROUP_JoanieRowan
    with dissolve

    jump p_2_5_rowan_or_joanie


label p_2_5_rowan_or_joanie:
    scene bg BG_FoyerNew
    with fade

    menu:
        "“What’s up with Rowan?”":
            jump p_2_5_1_whats_up_with_rowan
        "“What took you so long, Joanie?”":
            jump p_2_5_2_what_took_you_so_long


label p_2_5_1_whats_up_with_rowan:
    scene bg BG_FoyerNew
    with fade

    j "Anniversary with his girlfriend last night."
    j "Apparently they had words."
    f "He’ll live."

    "Joanie rubbed her forehead."

    j "Also—bus had to stop on that narrow road outside town."
    j "Dog on the bridge. Wouldn’t move."

    "That strange dog again."

    jump p_2_5_3_coinflip_setup


label p_2_5_2_what_took_you_so_long:
    scene bg BG_FoyerNew
    with fade

    j "Rowan was in a foul mood."
    j "And the bus had to stop on that narrow road outside town."
    j "Dog on the bridge. Wouldn’t move."

    "That strange dog again."

    jump p_2_5_3_coinflip_setup


label p_2_5_3_coinflip_setup:
    scene black
    show bg Dilemma2_5_CoinFlip
    with fade

    "Deciding who’d open the doors was a silly ritual, but we were fond of it."
    "We always used our shiny ‘lucky’ penny in a toss."

    f "Your turn to throw."
    "Joanie gave it a spin."
    j "Call!"
    play sound audio.sfx_coin

    menu:
        "Heads!":
            $ morality += 1
            $ popularity = 67
            "I called heads as the coin spun in the air."
            jump p_2_6_coin_rolls
        "Tails!":
            $ morality -= 1
            $ popularity = 33
            "I called tails, feeling like chancing it."
            jump p_2_6_coin_rolls


label p_2_6_coin_rolls:
    scene bg foyer
    with fade

    "The coin smacked onto the counter, wobbled…and rolled off the edge."
    "It disappeared under the counter into the dark."

    show joanie_unimpressed at right
    with dissolve

    j "Oh, for goodness’ sake..."

    "She crouched down to look for it, pushing aside boxes with one hand."

    menu:
        "Help Joanie look for the coin.":
            "I got down on my knees to help, but the coin had rolled too far under the counter."
            "We’d have to retrieve it later."
            j "You open. I’ll take care of the till."
            hide joanie_unimpressed
            with dissolve
            jump p_2_7_greet_audience

        "Run to the doors.":
            "While Joanie was busy, I opened the doors."
            "The crowd gave a half-cheer and started filing in."
            hide joanie_unimpressed
            with dissolve
            jump p_2_7_greet_audience


label p_2_7_greet_audience:
    scene bg foyer
    with fade

    "Town families, farmers in their Sunday best, kids already squabbling over who got the aisle seat."
    "I tore tickets, smiled until my cheeks hurt, dropped stubs into the metal bin at my feet."

    jump p_2_7_1_andykirstymoira_enter


label p_2_7_1_andykirstymoira_enter:
    scene bg foyer
    with fade

    show group_andykirstymoira at right
    with dissolve

    "Andy Thomas led the way to the back row, followed by his girlfriend Kirsty and her kid-sister Moira."

    menu:
        "“Andy,” I muttered in greeting.":
            "Andy ignored me and shoved past a couple of oldies."
            "Moira skipped after them."
            hide group_andykirstymoira
            with dissolve
            jump p_2_8_greet_orphans

        "“Hi Kirsty!”":
            "“Hi Frankie,” Kirsty said quickly, as Andy kept moving."
            "Moira skipped after them."
            hide group_andykirstymoira
            with dissolve
            jump p_2_8_greet_orphans

        "“Hi Moira!”":
            "Moira beamed."
            "“Hi Frankie!”"
            f "Enjoy the show."
            a "C’mon, Moira."
            hide group_andykirstymoira
            with dissolve
            jump p_2_8_greet_orphans


label p_2_8_greet_orphans:
    scene bg foyer
    with fade

    show group_nancy_abc at right
    with dissolve

    "Then came the kids from the orphanage and the mission, herded by Sister Nancy and Auntie Doris."
    "The front rows were theirs; they tumbled in like a litter of overexcited puppies."

    hide group_nancy_abc
    with dissolve

    "Little Alice called my name and I pretended to tug on a pigtail as she skipped past."

    jump p_2_8_2_greets_doris


label p_2_8_2_greets_doris:
    scene bg foyer
    with fade

    show doris_friendly at right
    with dissolve

    "And last came the mission mob of Aboriginal children led by their young auntie Doris—Mick’s daughter."

    menu:
        "“Hot walk into town, eh Doris?”":
            d "It’ll be hot when this movie’s done, Frankie."
            "One of the littlies piped up about the strange dog outside."
            "Doris frowned at that, but didn’t say more."
            hide doris_friendly
            with dissolve
            jump p_2_9_front_row_kids

        "“I saw Mick this morning.”":
            if stole_from_mick:
                d "This is a bad week for him each year."
                d "Hard family time for us."
                menu:
                    "I felt a twinge of regret about the money.":
                        "Something pinched at my gut, and I looked away."
                        hide doris_friendly
                        with dissolve
                        jump p_2_9_front_row_kids
                    "I told myself it would be put to good use.":
                        "I swallowed the thought and kept my face still."
                        hide doris_friendly
                        with dissolve
                        jump p_2_9_front_row_kids
            else:
                d "Yeah?"
                d "He’s around sometimes."
                hide doris_friendly
                with dissolve
                jump p_2_9_front_row_kids


label p_2_9_front_row_kids:
    scene bg auditorium_empty
    with fade

    show abc_happy at right
    with dissolve

    "I walked down to the front rows, checking that all the single seats were filled and no one was sitting on the floor."
    "The youngest kids wriggled in their chairs like jumping beans."

    menu:
        "“Settle down, you lot.”":
            "A few giggles. A few scowls."
            "Luckily the session was about to start."
            hide abc_happy
            with dissolve
            jump p_2_10_curtains_open
        "I let them wriggle.":
            "Luckily the session was about to start."
            hide abc_happy
            with dissolve
            jump p_2_10_curtains_open


label p_2_10_curtains_open:
    scene bg auditorium
    with fade

    "The curtains parted and the projector lit up the screen."

    menu:
        "God save our gracious King…":
            jump p_2_10_sing_anthem
        "I went about my duties.":
            jump p_2_10_1_joanie_unwell


label p_2_10_sing_anthem:
    scene bg auditorium
    with fade

    "The King’s portrait appeared, and the whole theatre stood to sing the anthem."
    "Voices filled the space: strong, shaky, off-key, all at once."

    jump p_2_10_1_joanie_unwell


label p_2_10_1_joanie_unwell:
    scene bg auditorium
    with fade

    show joanie_nauseous at right
    with dissolve

    "Partway through the newsreel, Joanie slipped into the aisle beside me, looking pale."

    j "Frankie… I don’t feel so good."

    menu:
        "“There’s Alka-Seltzer and Bex in the kitchen.”":
            f "There’s Alka-Seltzer and Bex in the kitchen."
            j "I don’t want medicine. I just want to not feel sick."
            jump p_2_10_5_joanie_vomits

        "“You hung-over again, Joanie?”":
            f "You hung-over again, Joanie?"
            j "No."
            j "…Maybe."
            jump p_2_10_5_joanie_vomits

        "“Don’t vomit here!”":
            f "Don’t vomit here!"
            "Cleaning up spew was my least favourite job."
            jump p_2_10_5_joanie_vomits


label p_2_10_5_joanie_vomits:
    scene bg foyer
    with fade

    "Just then, she brought her hands up to her mouth."
    "I grabbed an empty popcorn box and shoved it at her."

    f "Use this."

    "“SSHHH!” someone hissed from a row near us."

    "Joanie bolted up the aisle and out into the foyer."
    "I gave her a minute, then followed."

    j "I think I have food poisoning."
    j "You’ll manage, Frankie. I know you will."

    "Then she left."

    hide joanie_nauseous
    with dissolve

    "Other than Rowan upstairs, I was on my own until Mr Feros arrived."

    jump p_2_11_backrow_noisy


label p_2_11_backrow_noisy:
    scene bg auditorium
    with fade

    "Fewer than five minutes passed before the back row started horsing around."
    "Laughter. Whispers. The thud of feet on seats."

    "I flashed my torch their way."

    "A moment later, Andy and Kirsty and little Moira clambered down the steps and headed out into the foyer."

    jump p_2_11_1_counter


label p_2_11_1_counter:
    scene bg lolly_counter
    with fade

    show group_andy_kirstyemb at left
    with dissolve

    "They mucked about near the lolly counter, wasting my time."
    "Andy leaned on the counter like he owned it."

    a "Do you have beer?"

    "Kirsty blushed. She was obviously under-age."
    "This was a family theatre and we didn’t sell alcohol."

    menu:
        "“You got ID?”":
            jump p_2_11_3_andy_tries_buy_beer
        "“We don’t sell grog. Coke, raspberryade…”":
            jump p_2_11_6_andy_buys_cokes


label p_2_11_3_andy_tries_buy_beer:
    "Andy pulled out his driver’s licence, along with a wad of five-pound notes."
    f "Not a bad likeness."
    a "Two beers then."
    jump p_2_11_4_andy_fails_buy_beer


label p_2_11_4_andy_fails_buy_beer:
    f "Two beers—you’ll both have to be eighteen, or over."
    "Kirsty stared at the floor."
    jump p_2_11_5_andy_swore


label p_2_11_5_andy_swore:
    "Andy’s colour rose, and he swore under his breath."
    "They ordered Cokes and popcorn."
    f "Hey—Moira’s missing the cartoon."
    hide group_andy_kirstyemb
    with dissolve
    jump p_2_12_andy_wallet


label p_2_11_6_andy_buys_cokes:
    a "…and ginger beer."
    "They ordered Cokes and popcorn."
    f "Hey—Moira’s missing the cartoon."
    hide group_andy_kirstyemb
    with dissolve
    jump p_2_12_andy_wallet


label p_2_12_andy_wallet:
    scene black
    show bg Dilemma3_PreAndy
    with fade

    "Andy said he was going to take a leak first."
    "As he walked off, I noticed his wallet was just about to fall out of his back pocket."
    "It was bulging with cash."

    "What if I tripped him in the dark, and pinched the wallet?"
    "He’d never suspect me and no one else would be around."

    menu:
        "Trip Andy and steal the wallet.":
            $ stole_from_andy = True
            $ morality -= 2

            show bg Dilemma3_PostAndy
            with fade
            play sound audio.sfx_trip

            "As Andy pushed past me, I stuck my foot out just enough."
            "He stumbled."
            "In the confusion, my hand flicked out and the wallet was suddenly in my pocket."
            "He didn’t even realise."

            "The weight of it felt heavier than it had any right to."

            jump p_3_0_fire_start

        "Don’t touch Andy’s wallet.":
            $ stole_from_andy = False
            $ morality += 1

            scene bg auditorium
            with fade

            "The idea slid through my mind and out again."
            "Andy passed me in the dark and I let him go."

            jump p_3_0_fire_start



# ==========================================================
# ACT III – WHERE IS MR FEROS? (Twine-faithful)
# Passages covered: 3. Where is Mr Feros? → 3.6.1 Locked in
# ==========================================================

label p_3_0_fire_start:
    play music audio.act3 fadein 1.0
    scene bg BG_Auditorium
    with fade

    show Detail_ProjectionRoom_Rowan
    with dissolve

    "I’d been so busy, I realised I hadn’t told Rowan yet that it was just him and me on the shift."
    "Glancing up towards the projection booth, I saw two men inside, one of them wearing a hat."

    "It definitely wasn’t Mr Feros up there with Rowan."
    "Something ugly was going on."

    "The stranger had his back to the window. They were struggling, grappling with each other."

    menu:
        "I stepped back a few steps to see more clearly.":
            jump p_3_1_2_around_rowans_neck


label p_3_1_2_around_rowans_neck:
    scene bg BG_Auditorium
    with fade

    show Detail_ProjectionRoom_Rowan
    with dissolve

    "Light was pouring out from the projection booth."
    "Waves of dust mites and gusts of cigarette smoke wafted above the audience."

    "But I was almost certain the man’s hands were squeezing tight around Rowan’s neck."

    menu:
        "I quickly left the auditorium.":
            hide Detail_ProjectionRoom_Rowan
            with dissolve
            jump p_3_3_7_next_reel


label p_3_3_7_next_reel:
    scene bg BG_Hallway
    with fade

    "If I was attacked, who would put the feature film reel on?"
    "If it didn’t come on, people would be leaving their seats, standing up and looking around."

    "It would be chaos."

    menu:
        "Continue.":
            jump p_3_4_top_of_stairs


label p_3_4_top_of_stairs:
    scene bg BG_Hallway
    with fade

    show Detail_Door_Open
    with dissolve

    "At the top of the stairs, I looked along the gloomy corridor to the projection room."
    "Light from the open door fell out onto the floorboards."

    "Rowan always kept that door closed."

    menu:
        "I took a step closer.":
            jump p_3_4_1_sees_hand


label p_3_4_1_sees_hand:
    scene bg BG_Hallway
    with fade

    show Detail_Door_Open
    with dissolve

    "A man lay half in, half out of the room."
    "I wanted to go to him, but I also wanted to flee."

    menu:
        "I was too scared to move.":
            jump p_3_4_2_look_in_a_few_rooms

        "I ran to Rowan.":
            jump p_3_4_3_ran_to_him


label p_3_4_2_look_in_a_few_rooms:
    scene bg BG_Hallway
    with fade

    show Detail_Door_Open
    with dissolve

    "Then I edged forwards down the hallway, heart pounding, my back hard against the wall."
    "Then I heard a moan."

    "There was no question about it. It was Rowan all right."

    menu:
        "Continue.":
            jump p_3_4_3_ran_to_him


label p_3_4_3_ran_to_him:
    scene bg BG_ProjectionRoom
    with fade

    hide Detail_Door_Open
    with dissolve
    show Detail_Rowan
    with dissolve

    "He was trying to speak."
    "His neck was swollen and red. There were scratches and tear marks on his face."
    "He was struggling to sit up."

    "I knelt down to hear what he was saying."

    r "Change the reel!"
    r "C’mon, it needs to happen now."

    menu:
        "I changed the reel first.":
            jump p_3_4_4_change_reel

        "I called the police first.":
            jump p_3_4_7_call_police


label p_3_4_4_change_reel:
    scene bg BG_ProjectionRoom
    with fade

    show Detail_Rowan
    with dissolve

    f "Okay, but then I’m calling the police."

    "There was no sign of the man who’d attacked him, but a chair had been knocked over in the fight."
    "The reels were stacked in order."

    "We were into the final frames of the cartoon 'Soup’s On'."
    "Rowan had already mounted the first reel of 'The Third Man' onto the second projector."

    "Normally I’d be downstairs now getting ready with Joanie to sell drinks and popcorn."

    menu:
        "Continue.":
            jump p_3_4_5_changes_reel


label p_3_4_5_changes_reel:
    scene bg BG_ProjectionRoom
    with fade

    show Detail_Rowan
    with dissolve

    "But there was nothing normal about today."
    "‘No intermission today, folks,’ I said to myself."

    "I kept my eyes on the top right corner of the screen below us—every head in the audience turned toward the screen just as they should be."

    "There it was: the first black dot, the motor cue."

    "I started the feature’s first reel rolling."

    menu:
        "'Done.'":
            jump p_3_4_6_feros_office_hallway


label p_3_4_6_feros_office_hallway:
    scene bg BG_Hallway
    with fade

    hide Detail_Rowan
    with dissolve

    "Rowan gave me a thumbs-up."
    "I squeezed his hand, then trod cautiously along the hallway to Mr Feros’s office."

    "The door was closed."
    "I slowly opened it."
    play sound audio.sfx_opendoor

    "The door squeaked horrendously on its hinges."

    menu:
        "I winced.":
            jump p_3_5_inside_feros_office


label p_3_4_7_call_police:
    scene bg BG_Hallway
    with fade

    hide Detail_Rowan
    with dissolve

    f "It’ll take me two ticks to call the police."

    "I looked around the projection booth."
    "A chair had been knocked over in the fight."
    "The floor was a mess of ropes and cords, but the reels were stacked in order."

    "Rowan struggled to his feet and nodded."
    "I hoped he would be okay making the switch on his own."

    "I took off down the hall to Mr Feros’s office—where he should have been, but wasn’t."

    menu:
        "I opened the door wide.":
            jump p_3_5_inside_feros_office


label p_3_5_inside_feros_office:
    scene bg BG_Hallway
    with fade

    show Detail_Office
    with dissolve

    "The timber desk was scattered with pens, posters, flyers, a black telephone."
    "The in-tray was overflowing. Filing cabinet drawers were open."

    "All as usual."

    "No Mr Feros. No bodies. No strange man."

    "The guy must have fled the building. He’d be on his way out of town."

    menu:
        "I picked up the handset and dialled '213'.":
            jump p_3_5_1_phone_dead


label p_3_5_1_phone_dead:
    scene bg BG_Hallway
    with fade

    show Detail_Office
    with dissolve

    "No sound."
    "No lady asking 'Hello, how can I help you?'"

    "The line was dead."

    "All I could hear was the voices from the feature, still in the opening scenes."
    "The dead phone line was a very bad sign."

    menu:
        "Continue.":
            jump p_3_5_1_looks_for_2nd_phone


label p_3_5_1_looks_for_2nd_phone:
    scene bg BG_Hallway
    with fade

    hide Detail_Office
    with dissolve

    "There was another phone in the ticket booth."

    "But what if Rowan’s attacker was still lurking about somewhere?"
    "I didn’t like being alone."

    "Perhaps I should go check on Rowan."

    menu:
        "I went down to the ticket booth.":
            jump p_3_5_2_down_to_ticket_booth

        "I went back to the projection booth.":
            jump p_3_5_4_check_on_rowan


label p_3_5_2_down_to_ticket_booth:
    scene bg BG_FoyerNew
    with fade

    "I took the stairs down quietly, knowing which of them creaked and which to avoid."
    "My hearing in those minutes was acute."

    "A dog was barking in the distance."
    "There was a faint trace of a siren, and the murmurations of the film."

    "I lifted the ticket counter phone handset to my ear."
    "I knew what I was going to hear."

    ".    .    .    .    ."
    "Silence."

    menu:
        "Continue.":
            jump p_3_5_3_what_to_do


label p_3_5_3_what_to_do:
    scene bg BG_FoyerNew
    with fade

    show Rowan_Afraid at right
    with dissolve

    "It was dead."

    "Then I heard it—ca-thump, ca-thump, ca-thump."

    "I looked up the stairs."
    "So this was what a strangled man still alive crawled like."

    "Head bent, Rowan was inching his way along the first-floor hallway."
    "He was clutching at the red welts on his neck."

    menu:
        "I helped him down the stairs.":
            hide Rowan_Afraid
            with dissolve
            jump p_3_6_front_door_locked


label p_3_5_4_check_on_rowan:
    scene bg BG_Hallway
    with fade

    show Rowan_Afraid at right
    with dissolve

    "I turned back down the corridor towards the projection booth."

    "Then I heard it—ca-thump, ca-thump, ca-thump."

    "So, this was what a strangled man still alive crawled like."
    "Head bent, Rowan was inching his way along the floor."
    "He was clutching at the red welts on his neck."

    menu:
        "I helped him up onto his feet.":
            hide Rowan_Afraid
            with dissolve
            jump p_3_6_front_door_locked


label p_3_6_front_door_locked:
    scene bg BG_Foyer
    with fade

    "He needed a doctor urgently."

    f "Stay here. I’ll go down to the pub and use the phone there."
    play sound audio.sfx_opendoor

    "I strode over to the front door."
    "I tried to turn the handle."

    "It was jammed."

    menu:
        "I tried again, harder.":
            jump p_3_6_1_locked_in


label p_3_6_1_locked_in:
    scene bg BG_Foyer
    with fade

    "Worse. The door was locked."

    "The till was locked shut as it ought to be, but the keys behind it were gone."

    "I tried the kitchen and the back-stage doors."
    "All locked."

    "And Rowan was trying to tell me something."

    r "He’s going to..."

    "He paused."
    "He was still struggling to breathe."

    menu:
        "Going to what, Rowan?":
            jump p_3_13_end_of_act3


label p_3_13_end_of_act3:
    scene bg BG_Foyer
    with fade

    "Rowan’s eyes were wide."
    "Whatever he was trying to say, it was urgent."

    "Then—somewhere deeper in the building—something moved."
    "A sound that didn’t belong to the film."

    # Next in Twine is ACT IV (Frankie hears noises)
    jump p_4_0_frankie_hears_noises

# ==========================================================
# ACT IV – MAYHEM CONT., SEARCHING, HARRY REVEAL, LEVER SETUP
# Twine passages: 4. Frankie hears noises → 4.10.3 Pull lever option
# ==========================================================

label p_4_0_frankie_hears_noises:
    scene bg BG_Foyer
    with fade

    "Rowan’s eyes were wide."
    "Whatever he was trying to say, it was urgent."

    "Then—somewhere deeper in the building—something moved."
    "A sound that didn’t belong to the film."

    "A muffled thump. A scrape."
    "Like someone shifting weight behind a door."

    menu:
        "I went to the front windows.":
            jump p_4_1_front_windows
        "I checked the storeroom.":
            jump p_4_2_storeroom
        "I ran to the kitchen.":
            jump p_4_3_kitchen_check


# ----------------------------------------------------------
# 4.1 Front windows
# ----------------------------------------------------------
label p_4_1_front_windows:
    scene bg BG_FoyerNew
    with fade

    "I pressed up near the front windows and tried to see through the glare."
    "Outside, the street looked wrong—too bright, too still."

    "Then I saw it."
    "Smoke. Not far off now."

    "People were beginning to notice. Heads turning. Pointing."

    menu:
        "I checked the storeroom.":
            jump p_4_2_storeroom
        "I ran to the kitchen.":
            jump p_4_3_kitchen_check


# ----------------------------------------------------------
# 4.2 Storeroom
# ----------------------------------------------------------
label p_4_2_storeroom:
    scene bg BG_FoyerNew
    with fade

    "I swung open the storeroom door and peered inside."

    "Nothing but ice chests and stacks of empty lolly boxes."
    "No footsteps. No breathing. No hidden man."

    $ checked_icechests = True

    menu:
        "I ran to the kitchen.":
            jump p_4_3_kitchen_check
        "I went back toward Rowan.":
            jump p_4_3_4_back_to_rowan



# ----------------------------------------------------------
# 4.3 Kitchen check (stove / smoke check)
# ----------------------------------------------------------
label p_4_3_kitchen_check:
    scene bg BG_Kitchen
    with fade

    "The kitchen was empty."
    "The sink dripped."
    "The air felt hotter here."

    "My eyes flicked to the stove."

    menu:
        "I checked the stove.":
            jump p_4_3_1_checked_stove
        "I ran back out.":
            jump p_4_3_2_back_out


label p_4_3_1_checked_stove:
    scene bg BG_Kitchen
    with fade

    "Nothing burning."
    "No pot left on a flame."
    "No accident I could blame this on."

    $ checked_stove = True

    jump p_4_3_2_back_out


label p_4_3_2_back_out:
    scene bg BG_FoyerNew
    with fade

    "Back in the foyer, the film voices carried on like nothing was happening."
    "But the building felt… off."

    menu:
        "I checked the auditorium.":
            jump p_4_3_3_auditorium_check
        "I went back toward Rowan.":
            jump p_4_3_4_back_to_rowan


label p_4_3_3_auditorium_check:
    scene bg BG_Auditorium
    with fade

    "I slipped into the auditorium."
    "Everyone was still watching, faces turned toward the screen."
    "Cigarette smoke hung in the beam like fog."

    $ checked_auditorium = True

    "No one looked at me."
    "No one knew."

    jump p_4_3_4_back_to_rowan


label p_4_3_4_back_to_rowan:
    scene bg BG_FoyerNew
    with fade

    "I hurried back the way I’d come."

    "Rowan was still alive—but he wasn’t getting better."
    "He made a small sound, like he was trying to warn me again."

    "And then—below us—voices rose in the foyer."
    "Kids’ voices."

    jump p_4_4_kids_follow_frankie


# ----------------------------------------------------------
# 4.4 Kids follow Frankie
# ----------------------------------------------------------
label p_4_4_kids_follow_frankie:
    scene bg BG_FoyerNew
    with fade

    "A cluster of children had drifted out of the auditorium."
    "The orphan kids. The mission kids."

    "They stared up at me like I was meant to know what to do."
    "Like I was meant to fix this."

    menu:
        "I told them to get back inside.":
            jump p_4_4_1_tell_them_back_in
        "I told them to stay close.":
            jump p_4_4_2_stay_close


label p_4_4_1_tell_them_back_in:
    scene bg BG_FoyerNew
    with fade

    f "Back inside. Sit down. Watch the film."
    "They hesitated."
    "One kid sniffed and wiped his nose on his sleeve."

    jump p_4_4_3_nancy_appears


label p_4_4_2_stay_close:
    scene bg BG_FoyerNew
    with fade

    f "Stay close to me, alright?"
    "They clustered tighter, wide-eyed."

    jump p_4_4_3_nancy_appears


label p_4_4_3_nancy_appears:
    scene bg BG_FoyerNew
    with fade

    show Nancy_Worried at right
    with dissolve

    "Sister Nancy pushed through the foyer, flustered and sharp."

    n "Frankie! Have you seen my kids?"
    f "They’re right here—"

    "She counted quickly, lips moving."

    n "No. Not all."
    n "Alice, Craig, and Benjie—they’re missing."

    hide Nancy_Worried
    with dissolve

    jump p_4_5_nancy_lost_kids


# ----------------------------------------------------------
# 4.5 Sister Nancy’s lost kids
# ----------------------------------------------------------
label p_4_5_nancy_lost_kids:
    scene bg BG_FoyerNew
    with fade

    "My stomach dropped."
    "Three kids missing in a building that suddenly felt like a trap."

    "Somewhere deeper inside the Orpheum, I heard a faint sound."
    "A child’s cough—or a cry—half swallowed by walls."

    menu:
        "I ran upstairs.":
            jump p_4_6_run_upstairs
        "I searched downstairs first.":
            jump p_4_7_search_downstairs


label p_4_6_run_upstairs:
    scene bg BG_Hallway
    with fade

    "I took the stairs two at a time."
    "The hallway up here was darker now."
    "Hotter."

    "A door somewhere ahead clicked."
    "Not the sound of an audience door."
    "A small, private door."

    jump p_4_8_dress_circle_doors


label p_4_7_search_downstairs:
    scene bg BG_FoyerNew
    with fade

    "I ran along the downstairs corridor, checking doors I already knew were locked."
    "The sound came again—fainter this time."
    "Upstairs."

    "I swore under my breath and ran for the stairs."

    jump p_4_6_run_upstairs


label p_4_8_dress_circle_doors:
    scene bg BG_Hallway
    with fade

    "The dress-circle corridor felt like a throat—tight, dry, waiting to close."
    "I tried a door handle."

    "Locked."

    "Another."

    "Locked."

    "Then I saw it: a thin line of smoke, sneaking out from the crack beneath one door."

    jump p_4_9_harry_reveal


# ----------------------------------------------------------
# 4.9 Harry reveal (keys + gun)
# ----------------------------------------------------------
label p_4_9_harry_reveal:
    scene bg BG_Hallway
    with fade

    show Harry_Neutral_Gun at left
    with dissolve

    "A man stepped out of the shadows as if he’d been standing there the whole time."
    "Harry."

    "He held a gun in one hand and the Orpheum’s keys in the other."
    h "This theatre has so many hidey-holes."

    "I could smell his sweat though he stood a few feet away."

    menu:
        "Continue.":
            jump p_4_9_2_met_before


label p_4_9_2_met_before:
    scene bg BG_Hallway
    with fade

    show Harry_Gloating_Gun at left
    with dissolve

    "We’d met before."
    "He’d worked at the Orpheum for a couple of weeks, then Mr Feros had sent him off."
    "Didn’t like his lazy attitude."

    menu:
        "Give me back the keys, Harry.":
            jump p_4_9_3_asks_for_keys


label p_4_9_3_asks_for_keys:
    scene bg BG_Hallway
    with fade

    show Harry_Gloating_Gun at left
    with dissolve

    "I put my hand out for them."
    "For a moment he appeared indecisive."
    "I was trying to steady my shaking hand as I held it out."

    h "So many odd little rooms here, Frankie."

    menu:
        "I didn’t take my eyes off him.":
            jump p_4_10_harry_puts_andy_in_headlock


# ----------------------------------------------------------
# 4.10 Andy bursts in → callback → dilemma begins
# ----------------------------------------------------------
label p_4_10_harry_puts_andy_in_headlock:
    scene bg BG_Hallway
    with fade

    show GROUP_HarryGloating_AndyTerrified at left
    with dissolve

    "He was playing with me."

    "Just then Andy Thomas swung a door open."
    "It hit Harry as it opened."

    "Harry swung Andy down into a headlock, then pushed him away—arm outstretched, pistol at Andy’s temple."
    "Andy and I stood frozen to the spot."

    if stole_from_andy:
        jump p_4_10_callback_took_wallet
    else:
        jump p_4_10_callback_didnt_take_wallet


label p_4_10_callback_took_wallet:
    scene bg BG_Hallway
    with fade

    show GROUP_HarryGloating_AndyTerrified at left
    with dissolve

    "In that way that you remember or think something in a flash, I thought about the cash I’d taken from him."

    menu:
        "It didn’t make a difference to what was happening now.":
            jump p_4_10_1_dilemma_begins
        "It made me feel even worse for Andy.":
            jump p_4_10_1_dilemma_begins


label p_4_10_callback_didnt_take_wallet:
    scene bg BG_Hallway
    with fade

    show GROUP_HarryGloating_AndyTerrified at left
    with dissolve

    "In that way that you remember or think something in a flash, I was relieved that I hadn’t nicked Andy’s wallet."

    menu:
        "It didn’t make a difference now.":
            jump p_4_10_1_dilemma_begins
        "That I’d even considered it, made me feel worse for Andy.":
            jump p_4_10_1_dilemma_begins


label p_4_10_1_dilemma_begins:
    scene black
    show bg Dilemma4b_Lever_PreABC
    with fade

    show Harry_Gloating_Gun at left
    with dissolve

    h "Listen up, Frankie."
    h "There’s smoke being funnelled into the dressing room where I’ve locked up the three kids you’ve been looking for."
    h "Gee, I’ve forgotten their names already!"

    f "Alice, Craig, and Benjie."

    menu:
        "They’re just little tackers, Harry. Let them go.":
            jump p_4_10_2_do_nothing_option


label p_4_10_2_do_nothing_option:
    show bg Dilemma4a_Lever_PreMoira
    with fade

    show Harry_Gloating_Gun at left
    with dissolve

    h "But there’s this other girl, Moira, and she’s in the room above them."

    "He tapped Andy with the gun for emphasis."

    h "She’s safe for now."
    h "If you do nothing, I’ll unlock Moira’s room and let her out unharmed."

    menu:
        "Continue.":
            jump p_4_10_2b_do_nothing_option_2


label p_4_10_2b_do_nothing_option_2:
    scene bg BG_Hallway
    with fade

    show GROUP_HarryGloating_AndySobbing at left
    with dissolve

    "Andy began to quietly sob, begging Harry to please let her go."
    "Saying she was just a kid."

    h "What difference does it make what age they are?"

    menu:
        "It matters.":
            jump p_4_10_3_pull_lever_option


label p_4_10_3_pull_lever_option:
    scene bg BG_Hallway
    with fade

    show Harry_Gloating_Gun at left
    with dissolve

    h "Or, Frankie, you can push down on this lever here."

    "He pointed with his other hand to a lever and chain that snaked along the floor out of the room."

    # End of Act IV. Next is the actual moral choice (lever).
    # You can jump into your Act V / Choice 4 logic from here.
    jump p_5_choice_6_intro


# ==========================================================
# ACT V — TWINE-FAITHFUL (copy/paste this whole block)
# Covers:
# 5. CHOICE - do nothing or pull lever → 5.6.2 Explosion aftermath
# Then jumps to: 6. Returns to kitchen
#
# IMPORTANT (so you don't crash again):
# - Do NOT add any `default ...` lines in here. (You already hit “default X second time”.)
# - Make sure these vars exist ONCE somewhere earlier in your script:
#     default indecisive = False
#     default moira_dead = False
#     default kids_dead  = False
#     default feros_dead = False
#     default explosion  = False
# - Make sure these Characters exist ONCE:
#     define h = Character("Harry", ...)
#     define f = Character("Frankie", ...)
#     define r = Character("Rowan", ...)
# (Act VI uses Nancy later: define n = Character("Nancy", ...) — not used in Act V itself.)
# ==========================================================

# ------------------------------
# 5. CHOICE - do nothing or pull lever
# ------------------------------
label p_5_choice_6_intro:
    scene black
    show bg Dilemma4a_Lever_PreMoira
    with fade

    # If Harry sprite is meant to be present here:
    show Harry_Gloating_GunRaised at left
    with dissolve

    "'You've got 10 seconds. One, two...' The smell of his sweat and the blood pooling on the floor was sickening."
    "It was hard to think with him counting aloud."

    jump p_5_choice_6_pull_lever


label p_5_choice_6_pull_lever:
    # Twine link: [[Continue|CHOICE 6 - Pull the lever]]
    # We keep it as the actual choice menu here.

    # Clean up anything that might be lingering.
    $ explosion = False
    $ feros_dead = False
    $ indecisive = False

    menu:
        "Do nothing. (Kill 1)":
            jump p_5_1_1_do_nothing

        "Pull the lever. (Kill 3)":
            jump p_5_1_2_pull_lever
            play sound audio.sfx_lever

        # If you later add timeout logic, make it jump here:
        # (timer path)
        # "..." (hidden)
        #     jump p_5_1_3_timed_out_lever


# ------------------------------
# 5.1.1 Choice 1 - do nothing
# ------------------------------
label p_5_1_1_do_nothing:
    show bg Dilemma4a_Lever_PreMoira
    with fade

    hide Harry_Gloating_GunRaised
    with dissolve

    $ moira_dead = False
    $ kids_dead = True

    "I could not, would not push the lever."
    "Harry looked at his watch, counting out the long seconds. 'That should just about do it,' he said."
    "He watched me smugly, as I backed out of the room. I had to find Moira and at least try to free her."

    jump p_5_2_1_releases_moira


# ------------------------------
# 5.2.1 Releases Moira
# ------------------------------
label p_5_2_1_releases_moira:
    show bg Dilemma4a_Lever_PreMoira
    with fade

    "I didn't know which room she might be in. He'd said something about being above the other three."
    "I tried the short stairs to an upper balcony which we never used."
    "I could hear a faint voice crying out for help."
    "I found a door with a key right there, and unlocked it."
    "Moira rushed out into my arms, scared but unharmed."

    jump p_5_2_4_find_the_kids


# ------------------------------
# 5.2.4 Find the Kids
# ------------------------------
label p_5_2_4_find_the_kids:
    # Twine had hide-all-graphics + centre dialogue; we only keep narrative + flow.
    show bg Dilemma4a_Lever_PreMoira
    with fade

    "I found Moira at the top of the building, huddled and crying in a dusty, smoky upstairs cupboard."
    "He'd left the key outside the door."
    "I hurried her along and told her to find her sister and not let go."
    "Harry had said something about the three of them being below Moira."
    "There were so many rooms that we never used."
    "I called their names, but heard nothing in reply."
    "Then I saw smoke peeling out from underneath a doorway."
    " "
    "A rope was knotted around the door handle, tied tight to a hook hammered into the frame in a bowline knot."

    jump p_5_2_4_kids_dead


# ------------------------------
# 5.2.4 Kids dead
# ------------------------------
label p_5_2_4_kids_dead:
    show bg Dilemma4b_Lever_PostABC
    with fade

    "I flung open the door. Smoke billowed out, the heat was awful."
    "The children lay sprawled."
    "I dragged them out one by one, calling out to Nancy."
    "I didn't think she'd hear me, but she did."
    "I pulled Alice's hair away from her mouth, and bent over her hoping to feel her breath on my skin."
    " "
    "I was too late. They were all dead."

    jump p_5_3_mayhem_cont


# ------------------------------
# 5.1.2 Choice 2 - pull lever
# ------------------------------
label p_5_1_2_pull_lever:
    show bg Dilemma4b_Lever_PreABC
    with fade

    hide Harry_Gloating_GunRaised
    with dissolve

    $ moira_dead = True
    $ kids_dead = False

    "The metal of the lever was cold against the hot skin of my hand."
    "As soon as I felt the final clunk of the bolt into the shaft, I let go."
    "Harry watched me with a predatory look as I backed out of the room."
    "I had to find the kids."
    "Harry had killed Andy and I'd sent Moira to her death, but at least I could find the three kids and set them free."

    jump p_5_2_2_releases_orphan_kids


# ------------------------------
# 5.2.2 Releases orphan kids
# ------------------------------
label p_5_2_2_releases_orphan_kids:
    show bg Dilemma4b_Lever_PreABC
    with fade

    "I ran down the Dress Circle hallway, flinging doors open."
    "I could hear their young voices crying out for help."
    "I found a door with a key right there, and unlocked it."
    "The children fell out, coughing, but alive."
    "I hurried them towards the stairs, calling out for Nancy."
    "We needed to get everyone into the kitchen downstairs."

    jump p_5_2_3_find_moira


# ------------------------------
# 5.2.3 Find Moira
# ------------------------------
label p_5_2_3_find_moira:
    show bg Dilemma4b_Lever_PreABC
    with fade

    "With the three orphans back in Nancy's arms, I had to find Moira."
    "I tried the short stairs to an upper balcony. He'd said something about her being above the others."
    "This corridor was dark. We never used these rooms."
    "I called her name."
    "A key was lying on the floor."
    "I tried each door with it."
    " "
    "I could smell the smoke getting stronger as I went to each of the doors."
    "At last it fit."

    jump p_5_2_4_moira_dead


# ------------------------------
# 5.2.4 Moira dead
# ------------------------------
label p_5_2_4_moira_dead:
    show bg Dilemma4a_Lever_PostMoira
    with fade

    "There she was, small and crumpled, amidst the smoke and heat."
    "She was dead."
    "I carried her downstairs."
    "People rushed forward and took her from me."

    jump p_5_3_mayhem_cont


# ------------------------------
# 5.1.3 Timed out lever  (NOT wired to a timer yet — you said later)
# ------------------------------
label p_5_1_3_timed_out_lever:
    $ indecisive = True
    $ moira_dead = True
    $ kids_dead = True

    show bg Dilemma4a_Lever_PreMoira
    with fade

    show Harry_Gloating_GunRaised at left
    with dissolve

    "Harry unlocked the chain from the lever. It was too late to push on it."
    "'All four kids are going to pay for your indecision now, Frankie.'"
    "He kept the pistol pointed at me as he opened the door to leave."
    "I was frozen to the spot."
    "'Better luck making up your mind next time,' he said, and left."
    "I couldn't stop trembling, caught between Andy lying dead on the floor and the door."

    jump p_5_1_4_timed_out_lever_cont


label p_5_1_4_timed_out_lever_cont:
    scene bg BG_Kitchen
    with fade

    hide Harry_Gloating_GunRaised
    with dissolve

    "I could hear glass breaking, banging and sobbing, a dog barking and children wailing. The smell of smoke was stronger."
    "In the kitchen, some women had found buckets and were filling them at the sink."

    jump p_5_1_5_buckets_despair


label p_5_1_5_buckets_despair:
    scene bg BG_Kitchen
    with fade

    "A few buckets of water wouldn't go far."
    "I was filled with a feeling of despair."
    "And I hated myself for being so indecisive."
    "All four of the children would be dead by now."

    jump p_5_3_1_returns_to_theatre


# ------------------------------
# 5.3 Mayhem cont.
# ------------------------------
label p_5_3_mayhem_cont:
    scene bg BG_Kitchen
    with fade

    "I could hear glass breaking, banging and sobbing, a dog barking and children wailing."
    "The smell of smoke was stronger."
    "In the kitchen men were heaving themselves against the door, but it was a strong cedar door with iron bracing."
    "Two women had found buckets and were filling them at the sink."
    ""
    "A few buckets of water wouldn't go far."

    jump p_5_3_1_returns_to_theatre


# ------------------------------
# 5.3.1 returns to theatre
# ------------------------------
label p_5_3_1_returns_to_theatre:
    scene bg BG_Auditorium
    with fade

    "In the foyer, men had made a battering-ram from chairs."
    "A woman grasped me by my shoulders and shook me, crying at me to unlock the doors."
    "I ran back into the cavernous theatre, blinking back tears."
    ""
    "Then I again heard Harry's courteous, evil voice."

    jump p_5_4_sees_mr_feros_on_chair


# ------------------------------
# 5.4 Sees Mr Feros on chair
# ------------------------------
label p_5_4_sees_mr_feros_on_chair:
    scene bg BG_Auditorium
    with fade

    # Twine shows Detail_ProjectionRoom_Feros on the right.
    show Detail_ProjectionRoom_Feros
    with dissolve

    "'Frankie, we're not finished yet.' Silhouetted against the light, Harry spoke to me from the projection room."
    "Then he stepped decisively to one side."
    "Mr Feros, my boss, was standing on what must have been a chair."
    "He had a noose around his neck and his arms were tied."
    "His face wore a look of terror."
    ""
    "'Come,' said Harry."

    menu:
        "I trembled as I went up the stairs.":
            jump p_5_4_1_back_in_projection_booth
        "I was ready for whatever he had.":
            jump p_5_4_1_back_in_projection_booth


# ------------------------------
# 5.4.1 Frankie back in projection booth
# ------------------------------
label p_5_4_1_back_in_projection_booth:
    scene bg BG_ProjectionRoom_MrFeros
    with fade

    hide Detail_ProjectionRoom_Feros
    with dissolve

    show Harry_Neutral_Gun at left
    with dissolve

    "Harry gestured at me to close the door behind us."
    "Mr Feros's eyes were boring into mine, pleading with me."

    menu:
        "I launched myself at Harry.":
            jump p_5_4_2_attack_harry
        "I let him talk.":
            jump p_5_4_3_harry_explains_choices


# ------------------------------
# 5.4.2 Attack Harry
# ------------------------------
label p_5_4_2_attack_harry:
    scene bg BG_ProjectionRoom_MrFeros
    with fade

    show Harry_Angry_GunRaised at left
    with dissolve

    "Quick as a flash he had my arm behind my back and his gun to my head."
    ""
    "'Tsk, tsk, Frankie. You won't be able to save anyone if you're dead, now will you?'"

    jump p_5_4_3_harry_explains_choices


# ------------------------------
# 5.4.3 Harry explains choices
# ------------------------------
label p_5_4_3_harry_explains_choices:
    show bg Dilemma5a_PreFeros
    with fade

    hide Harry_Angry_GunRaised
    hide Harry_Neutral_Gun
    with dissolve

    "'Like I said, you get to choose. I can detonate a small bomb which will kill three people. Not that many really."
    "Or, you can kick this chair out from under the boss's feet.'"
    ""
    "I kept my eyes down, avoiding looking at the chair with Mr Feros standing on it."
    "I also didn't want to know who the three people were. Knowing would make it worse."

    jump p_5_4_4_harry_explains_choices_again


# ------------------------------
# 5.4.4 Harry explains choices again
# ------------------------------
label p_5_4_4_harry_explains_choices_again:
    show bg Dilemma5a_PreFeros
    with fade

    "'Frankie? Would you prefer I set off the explosion, three dead, hands-free for you?"
    "Or would you rather hang the man? In which case, there'll be no explosion, just one death, but with the proverbial 'blood on your hands'.'"
    "I had never before felt such dread."
    "'Frankie, you don't have time to ponder. You can trust me to light the fuse, or trust yourself to kick the chair."
    "Time to decide. My wick is short.'"

    jump p_5_4_5_harry_impatient


# ------------------------------
# 5.4.5 Harry impatient → CHOICE 7
# ------------------------------
label p_5_4_5_harry_impatient:
    show bg Dilemma5a_PreFeros
    with fade

    "He shook me roughly. 'If you don't hurry up, then I'll kick the chair and light the fuse. That'll be four dead!'"
    ""
    "It was time."

    jump p_5_choice_7_kick_the_chair


# ------------------------------
# CHOICE 7 - Kick the chair
# ------------------------------
label p_5_choice_7_kick_the_chair:
    # If you later add a timer: timeout should jump to p_5_6_timed_out_kick_chair
    menu:
        "Kick the chair (kill 1).":
            jump p_5_5_1_kick_chair_kill_1

        "Refuse to kick it (explosion kills 3).":
            jump p_5_5_3_explosion_kill_3


# ------------------------------
# 5.5.1 Choice - Kick chair kill 1
# ------------------------------
label p_5_5_1_kick_chair_kill_1:
    show bg Dilemma5a_PreFeros
    with fade

    $ feros_dead = True
    $ explosion = False

    "I avoided looking at Mr Feros as I approached him. He'd always been a nice guy."
    ""
    "I could feel the fear streaming off him."

    jump p_5_5_2_pulls_chair_out_kills_boss


label p_5_5_2_pulls_chair_out_kills_boss:
    show bg Dilemma5a_PostFeros
    with fade
    play sound audio.sfx_kickchair

    "Tears streamed down my face as I yanked the chair as hard as I could from out beneath him."
    "I ran from the room as his body writhed, Harry's laughter behind me."

    jump p_5_5_2b_breaks_wick


label p_5_5_2b_breaks_wick:
    show bg Dilemma5a_PostFeros
    with fade

    "Along the skirting-board I saw the wick that led to the locked room down the hall."
    "Harry had tacked it down neat alongside the wall. I wrenched it in two."
    ""
    "'We'll get you out!' I yelled down the hallway. I didn't know how, but we would."

    jump p_6_0_returns_to_kitchen


# ------------------------------
# 5.5.3 Choice - Explosion Kill 3
# ------------------------------
label p_5_5_3_explosion_kill_3:
    scene bg BG_ProjectionRoom
    with fade

    $ explosion = True
    $ feros_dead = False

    "'I won't kick that chair.'"
    "Harry flicked his lighter, then knelt down and held it to a long wick that ran out of the room snaking its way to where the three were trapped."
    "Gun in hand, he left to watch the wick burn down the long hallway."
    "My hands shook mightily as I untied Mr Feros's hands. He loosened the noose and pulled himself free."
    ""
    play sound audio.sfx_bomb
    "'Frankie' he said, embracing me. 'Thank you, thank you,' he was still saying as we heard the explosion."

    jump p_5_5_4_finds_three_dead


label p_5_5_4_finds_three_dead:
    show bg Dilemma5b_PostExplosion
    with fade

    "'Be careful then,' Mr Feros said."
    "I ran down through the billowing dust and smoke, clambering over the broken plaster and split timbers towards the room the  group had been held in."
    "The floor gaped. A large hole had been torn through it. They had fallen to their deaths onto the auditorium below."
    ""
    "I watched as tiny grains of brick and gyprock floated through the air."

    jump p_6_0_returns_to_kitchen


# ------------------------------
# 5.6 Timed out kick chair  (NOT wired to a timer yet)
# ------------------------------
label p_5_6_timed_out_kick_chair:
    $ indecisive = True
    $ feros_dead = True
    $ explosion = True

    scene bg BG_ProjectionRoom
    with fade

    "Harry flicked his lighter, then kneeling down, he held the flame to a long wick that ran out of snaked its way to where the three were trapped."
    "Then with a mighty kick, Harry shot the chair out from under Mr Feros."

    jump p_5_6_1_noose_and_explosion


label p_5_6_1_noose_and_explosion:
    scene bg BG_ProjectionRoom
    with fade

    "I could hear my boss writhing, then the slump. It wasn't a quick death."
    play sound audio.sfx_bomb
    "And then the explosion. Harry had killed all four."
    "I'd not been quick enough."

    jump p_5_6_2_explosion_aftermath


label p_5_6_2_explosion_aftermath:
    show bg Dilemma5b_PostExplosion
    with fade

    "I ran down through the billowing dust and smoke, clambering over the broken plaster and split timbers towards the room the group had been held in."
    "The floor gaped. A large hole had been torn through it. They had fallen to their deaths onto the auditorium below."
    ""
    "I watched as tiny grains of brick and gyprock floated through the air."

    jump p_6_0_returns_to_kitchen

# ==========================================================
# ACT VI — RETURNS TO KITCHEN (Twine-faithful)
# Passages:
# 6. Returns to kitchen → 6.7 Mick goes to pub
# Then links to:
# 7. Barricaded doors against smoke
#
# NOTES:
# - Do NOT add any `default ...` here (you already hit "default given a second time").
# - Requires these images to be defined somewhere:
#   BG_Kitchen, Rowan_Stoic, Doris_Singing, Nancy_Praying,
#   Detail_Dog, Mick_Neutral, Mick_Concerned
# - Uses vars:
#   kicked_the_dog, feros_dead, explosion
# ==========================================================

# Entry label used by Act V (keep this name).
label p_6_0_returns_to_kitchen:
    jump p_6_returns_to_kitchen


label p_6_returns_to_kitchen:
    scene bg BG_Kitchen
    with fade

    # Twine: hide-all-graphics, centre dialogue
    # We emulate by clearing sprites.
    hide Rowan_Stoic
    hide Doris_Singing
    hide Nancy_Praying
    hide Detail_Dog
    hide Mick_Neutral
    hide Mick_Concerned
    with dissolve

    "I found Doris and Sister Nancy sitting cross-legged with their kids around them. Doris was singing quietly, Nancy praying. All the children and parents had gathered now in the kitchen, scared and silent."
    " "
    "I noticed Rowan leaning against the wall in the corner by the stove."

    menu:
        "I embraced Rowan.":
            jump p_6_1_embraces_rowan
        "I listened to Doris' singing.":
            jump p_6_2_doris_sings
        "I joined Nancy in prayer.":
            jump p_6_3_pray_with_nancy


label p_6_1_embraces_rowan:
    scene bg BG_Kitchen
    with fade

    show Rowan_Stoic at right
    with dissolve

    "'I'm so glad you're alive.'"
    " "
    "He put his arms around me and squeezed hard. Tears streaked down my face. Were we all going to die in the inevitable inferno?"

    jump p_6_2_hears_a_dog_barking


label p_6_2_doris_sings:
    scene bg BG_Kitchen
    with fade

    show Doris_Singing at right
    with dissolve

    "'Sad song?' I asked Doris, hiding myself down beside her and the children."
    "'No. A song of hope.' Her dark eyes were confident and clear. I wanted to believe her."

    menu:
        "'I don't feel hopeful.'":
            jump p_6_2_1_doris_sings_2


label p_6_2_1_doris_sings_2:
    scene bg BG_Kitchen
    with fade

    show Doris_Singing at right
    with dissolve

    "'Mick'll come save us, if he's nearby.'"
    "'You think?'"
    "'Spirit connection. He'll know something's wrong here.'"
    "I wanted to believe her."

    jump p_6_2_hears_a_dog_barking


label p_6_3_pray_with_nancy:
    scene bg BG_Kitchen
    with fade

    show Nancy_Praying at right
    with dissolve

    "'Even when I walk in the valley of darkness,"
    "I will fear no evil for You are with me;"
    "Your rod and Your staff-they comfort me.'"
    " "
    "I felt a little calmer."

    jump p_6_2_hears_a_dog_barking


label p_6_2_hears_a_dog_barking:
    scene bg BG_Kitchen
    with fade

    # Twine: Detail_Dog graphic, dialogue right
    show Detail_Dog at left
    with dissolve

    "Had it only been half an hour since the terror had started? Time shrank and stretched. Now I could hear a dog barking close by."
    "I looked out the window. I'd be damned. It was the same dog that had been out the front this morning."

    if kicked_the_dog:
        "Kicking it hadn't done a thing to drive it away. Its barking was really getting to me."
    else:
        "Why it wanted to hang around here all morning, I didn't know. Poor old thing, it looked so mangy."

    jump p_6_2_doris_sings_dog_barks_nancy_praying


label p_6_2_doris_sings_dog_barks_nancy_praying:
    scene bg BG_Kitchen
    with fade

    hide Detail_Dog
    with dissolve

    "Doris continued to sing with her quiet, sweet voice, the children close around her. That mongrel outside was barking. Sister Nancy prayed with her eyes fixed on the children."
    " "

    if feros_dead:
        "I wished Mr Feros was still with us."
        if not explosion:
            "I avoided the eyes of the three whom I'd saved instead."
    else:
        "Mr Feros was moving between the groups of parents and children trying to reassure them. Like me, he wasn't saying anything to them about what he'd been through, or about the others whom Harry had killed. There'd be time for talking later."

    jump p_6_4_sees_mick_out_back


label p_6_4_sees_mick_out_back:
    scene bg BG_Kitchen
    with fade

    show Mick_Neutral at right
    with dissolve

    "Then through the window I saw old Mick half a dozen feet away in the back lane, staring gloomily at the dog."

    menu:
        "I leapt up.":
            jump p_6_5_yells_out_window_to_mick


label p_6_5_yells_out_window_to_mick:
    scene bg BG_Kitchen
    with fade

    show Mick_Concerned at right
    with dissolve

    "Wrapping my hand in a couple of towels, I punched through a pane of glass behind the bars."
    "Now we had his attention. Mick peered in at me through the broken glass."
    "'Hey. What's up with the kiddies?'"
    "'We're trapped, can't you smell the fire?'"

    menu:
        "'Mick, we need help here.'":
            jump p_6_7_mick_goes_to_pub


label p_6_7_mick_goes_to_pub:
    scene bg BG_Kitchen
    with fade

    show Mick_Concerned at right
    with dissolve

    "'I don't want no trouble at the pub,' said Mick gruffly."
    "'Yeah, call out to Brenda to get the cops and the fire-brigade.'"
    "Mick strode off on his lean and bent stockman's legs."
    "Maybe, just maybe, some of us were going to get out alive."

    menu:
        "'And axes, Mick!'":
            # Twine link goes to: 7. Barricaded doors against smoke
            jump p_7_barricaded_doors_against_smoke


# ----------------------------------------------------------
# Stub label to prevent crashes until Act VII is pasted in.
# Replace this jump target with your real Act VII entry label if needed.
# ----------------------------------------------------------


# ==========================================================
# ACT VII – Barricaded doors against smoke  → gun choice
# ACT VIII – Firefighters take over
# ACT IX – Frankie looks for Rowan → outcomes → callbacks
# ACT X – Aftermath / final passage
# Twine-faithful from your HTML export.
# ==========================================================

# NOTE: This block assumes these variables already exist (define ONCE in your defaults):
# indecisive (bool), timed_out_harry (bool), harry_dead (bool),
# feros_dead (bool), explosion (bool),
# moira_dead (bool), kids_dead (bool)
#
# Do NOT "default" them again if you already have them; Ren'Py will throw "default ... second time".

label p_7_barricaded_doors_against_smoke:
    play music audio.act4 fadein 1.0
    scene bg BG_Foyer
    with fade

    "For now, we barricaded the doors against smoke. We used chairs, heavy boxes, anything we could find."
    "We prayed the smoke would go somewhere else."
    "We waited."

    jump p_7_1_hears_the_dog_barking


label p_7_1_hears_the_dog_barking:
    scene bg BG_Kitchen
    with fade

    "Then I heard it again."
    "A dog barking, somewhere close."
    "And above that—footsteps."

    jump p_7_2_kirsty_at_the_kitchen


label p_7_2_kirsty_at_the_kitchen:
    scene bg BG_Kitchen
    with fade

    show Detail_Kirsty
    with dissolve

    "Kirsty appeared in the doorway, coughing, her eyes wide with panic."

    jump p_7_3_kirsty_says_harry


label p_7_3_kirsty_says_harry:
    scene bg BG_Kitchen
    with fade
    show Detail_Kirsty
    with dissolve

    "‘Harry’s still in here,’ Kirsty said."
    "‘He’s got a gun.’"

    menu:
        "Continue.":
            jump p_7_4_harry_at_the_doors


label p_7_4_harry_at_the_doors:
    scene bg BG_Foyer
    with fade

    "We could hear him at the front."
    "The barricade shuddered as something heavy slammed into it."

    jump p_7_5_the_doors_splinter


label p_7_5_the_doors_splinter:
    scene bg BG_Foyer
    with fade

    "The doors splintered."
    "Smoke rolled in like a living thing."

    menu:
        "Continue.":
            jump p_7_6_harry_points_gun


label p_7_6_harry_points_gun:
    show bg Dilemma6_PreHarry
    with fade

    show Harry_Gloating_GunRaised at left
    with dissolve

    "Harry stood there in the smoke, gun in hand, grinning."
    "‘Well,’ he said. ‘Look at you all.’"

    jump p_7_7_nancy_shouts


label p_7_7_nancy_shouts:
    show bg Dilemma6_PreHarry
    with fade

    show Harry_Gloating_GunRaised at left
    with dissolve

    n "Frankie! Have you seen my kids?"

    "My stomach turned over."

    jump p_7_8_harry_talks_gun


label p_7_8_harry_talks_gun:
    show bg Dilemma6_PreHarry
    with fade

    show Harry_Gloating_GunRaised at left
    with dissolve

    "Harry waved the gun lazily, like he was conducting us."

    h "You’re all going to do what I say."
    h "Or I’ll shoot."

    menu:
        "Continue.":
            jump p_7_9_choice_wait_or_shoot


# ----------------------------------------------------------
# 7.9 CHOICE – Wait for police vs Shoot Harry
# (Twine: morality += morality OR morality -= morality)
# ----------------------------------------------------------
label p_7_9_choice_wait_or_shoot:
    show bg Dilemma6_PreHarry
    with fade

    show Harry_Gloating_GunRaised at left
    with dissolve

    "I had the gun."
    "I could feel its weight in my hands."

    menu:
        "Wait for the police.":
            # Twine: (change-morality: +$morality) (set-popularity: 95)
            $ morality += morality
            $ popularity = 95
            $ harry_dead = False
            $ timed_out_harry = False
            jump p_7_9_1_callback_saved_harry

        "Shoot Harry.":
            # Twine: (change-morality: -$morality) (set-popularity: 5)
            $ morality -= morality
            $ popularity = 5
            $ harry_dead = True
            $ timed_out_harry = False
            jump p_7_9_2_callback_shot_harry

        # If you later re-enable timed choices, route your timeout to p_7_9_4_timed_out_harry_laughs


label p_7_9_1_callback_saved_harry:
    scene bg BG_Foyer
    with fade

    "We waited."
    "Time stretched, thin as paper."

    jump p_8_firefighters_take_over


label p_7_9_2_callback_shot_harry:
    scene bg BG_Foyer
    with fade
    play sound audio.sfx_gunshot

    "I squeezed the trigger."
    "The sound was enormous in the cramped air."

    jump p_8_firefighters_take_over


label p_7_9_4_timed_out_harry_laughs:
    # Twine equivalent exists as a “timed out” branch; keep this label so you can hook timers later.
    # If your Twine run timed out here, set:
    # $ timed_out_harry = True
    # and probably:
    # $ indecisive = True
    scene bg BG_Foyer
    with fade

    "I froze."
    "Harry laughed."

    $ timed_out_harry = True
    $ indecisive = True

    jump p_8_firefighters_take_over


# ==========================================================
# ACT VIII – Firefighters take over
# ==========================================================
label p_8_firefighters_take_over:
    scene bg BG_Foyer
    with fade

    "Eventually the firemen came. They took over. They took us out into the street. The police took our details."
    "The firemen put blankets around us. They brought out the dead and injured."
    "If I had been outside, I might have passed out, seeing it all. But I'd been in it."
    "Somehow, the horror of it all felt real, but distant."

    jump p_8_1_there_were_questions


label p_8_1_there_were_questions:
    scene bg BG_Foyer
    with fade

    "There were going to be questions."
    "There were going to be rumours."
    "There were going to be headlines."

    jump p_9_frankie_looks_for_rowan


# ==========================================================
# ACT IX – Frankie looks for Rowan → callbacks and wrap-up
# ==========================================================
label p_9_frankie_looks_for_rowan:
    scene bg BG_Outro_Alternative
    with fade

    show Rowan_Stoic at right
    with dissolve

    "'Frankie! Did you see the boss?' Rowan asked. 'Where was he? What happened?'"

    menu:
        "Not sure.":
            jump p_9_1_not_sure_branch
        "Yes.":
            jump p_9_1_yes_branch


label p_9_1_not_sure_branch:
    # Twine logic:
    # (if: $feros_dead and $explosion) -> 9.1.3
    # (else-if: $feros_dead) -> 9.1.1
    # (else:) -> 9.1.2
    if feros_dead and explosion:
        jump p_9_1_3_callback_timed_out_final_4
    elif feros_dead:
        jump p_9_1_1_callback_kick_chair_kill_1
    else:
        jump p_9_1_2_callback_explosion_kill_3


label p_9_1_yes_branch:
    if feros_dead and explosion:
        jump p_9_1_3_callback_timed_out_final_4
    elif feros_dead:
        jump p_9_1_1_callback_kick_chair_kill_1
    else:
        jump p_9_1_2_callback_explosion_kill_3


label p_9_1_1_callback_kick_chair_kill_1:
    scene bg BG_Outro_Alternative
    with fade

    show Rowan_Stoic at right
    with dissolve

    "I couldn't bear to tell Rowan what I'd done."
    "That Mr Feros was dead because of me."
    "And that I'd done it to save those three kids."

    jump p_9_2_processing


label p_9_1_2_callback_explosion_kill_3:
    scene bg BG_Outro_Alternative
    with fade

    show Rowan_Stoic at right
    with dissolve

    "I told him I'd found Mr Feros."
    "That he'd been alive."
    "And that then the explosion happened."

    jump p_9_2_processing


label p_9_1_3_callback_timed_out_final_4:
    scene bg BG_Outro_Alternative
    with fade

    show Rowan_Stoic at right
    with dissolve

    "I told Rowan the truth."
    "That I'd frozen."
    "That Harry had killed Mr Feros."
    "And then the explosion."
    "Harry had killed all four."

    jump p_9_2_processing


label p_9_2_processing:
    scene bg BG_Outro_Alternative
    with fade

    hide Rowan_Stoic
    with dissolve

    "No one knew yet of all the choices I'd been given."

    if indecisive:
        jump p_9_2_4_indecisive_done_better
    else:
        jump p_9_2_1_did_my_best


label p_9_2_1_did_my_best:
    scene bg BG_Outro_Alternative
    with fade

    "When they did, I hoped they'd know that I'd not just gone and hid, or given up doing the best that I could."
    "All around me parents and children were hugging and crying, sharing what had happened, but I had no one to talk to."

    jump p_9_3_pick_harry_callback


label p_9_2_4_indecisive_done_better:
    scene bg BG_Outro_Alternative
    with fade

    "For now, no one knew of all the choices I'd been given. When they did, I hoped they'd know that I'd not given up doing the best that I could."
    "But the fact was, if I'd been more decisive, I could have saved more lives. But whose?"
    ""
    "All around me parents and children were hugging and crying, sharing what had happened. But I had no one."

    jump p_9_3_pick_harry_callback


label p_9_3_pick_harry_callback:
    if timed_out_harry:
        jump p_9_3_3_callback_timed_out_shot_harry
    elif harry_dead:
        jump p_9_3_2_callback_shot_harry
    else:
        jump p_9_3_1_callback_saved_harry


label p_9_3_1_callback_saved_harry:
    scene bg BG_Outro_Alternative
    with fade

    show Rowan_Stoic at right
    with dissolve

    "We watched Harry get loaded into an ambulance with a policeman alongside, get driven off to the hospital."
    "'He doesn't deserve a bed,' said Rowan. The mangy dog cantered after the ambulance. So, it really had been Harry's mutt all along. I'd been warned right from the start."

    jump p_10_aftermath_1


label p_9_3_2_callback_shot_harry:
    scene bg BG_Outro_Alternative
    with fade

    show Rowan_Stoic at right
    with dissolve

    "We watched Harry get wrapped in a sheet. The ambulances were full, so he just lay there next to a police car."
    "The mangy dog sat a few feet away. So, it really had been Harry's mutt all along. I'd been warned right from the start."

    jump p_10_aftermath_1


label p_9_3_3_callback_timed_out_shot_harry:
    scene bg BG_Outro_Alternative
    with fade

    show Rowan_Stoic at right
    with dissolve

    "We watched Harry get loaded into an ambulance with a policeman alongside."
    "'He doesn't deserve to live,' I said."
    "'Let alone a hospital bed,' said Rowan. 'What a bastard.'"
    "The van left for the hospital, with the mangy dog cantering along behind it. So, it really had been Harry's mutt all along. I'd been warned right from the start."

    jump p_10_aftermath_1


# ==========================================================
# ACT X – Aftermath / ending
# ==========================================================
label p_10_aftermath_1:
    scene bg BG_Outro_Alternative
    with fade

    hide Rowan_Stoic
    with dissolve

    "I just hadn't known it."

    jump p_10_1_aftermath_2


label p_10_1_aftermath_2:
    scene bg BG_Outro_Alternative
    with fade

    "By now, there was just a few of us standing around watching the fire burn."
    "The firemen tried to save the building. It wasn't to be."
    "Our beloved Orpheum burned slowly to the ground. It was gone."
    "Now the questions were going to start"

    jump p_10_2_final_passage


label p_10_2_final_passage:
    scene bg BG_Outro_Alternative
    with fade

    "Everyone would want to know what I'd done, and why. What was I going to tell them?"
    "I was afraid of what was to come. I had just been the usher in town, friendly Frankie, but now? Who was I now?"

    $ path = export_log_csv("mayhem_run.csv")
    "Saved to: [path]"



    return
