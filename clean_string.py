# TODO: Turn this into a package


def clean_string(input):
    import re

    def do(input):
        # Make sure input is a string
        input = input if type(input) is str else ''

        # Turn everything into lower case
        input = input.lower()

        # Remove characters with numbers
        input = re.sub(r"\S*\d+\S*", ' ', input, 0)

        # Transform fancy characters to normal ones (taken from: https://gist.github.com/zerolab/1633661)
        input = re.sub(r'[\x84\x93\x94]', '"', input, 0)
        input = re.sub(r'[\u201C\u201D\u201E\u201F\u2033\u2036]', '"', input, 0)
        input = re.sub(r"[\u2018\u2019\u201A\u201B\u2032\u2035]", "'", input, 0)
        input = re.sub(r"[\x82\x91\x92]", "'", input, 0)

        # Remove stray hyphens and apostrophes
        input = re.sub(r"(?<=\s)\-(?=\s)|(?<=.)\-(?=\s)|(?<=\s)\-(?=.)|^\-(?=.)|(?<=.)\-$", ' ', input, 0)
        input = re.sub(r"(?<=\s)\'(?=\s)|(?<=.)\'(?=\s)|(?<=\s)\'(?=.)|^\'(?=.)|(?<=.)\'$", ' ', input, 0)

        # Remove remove HTML tags
        input = re.sub(r"<.*?\>", ' ', input, 0)
        input = re.sub(r"&.*?;", ' ', input, 0)

        # Remove links (taken from https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url)
        input = re.sub(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", ' ', input, 0)
        input = re.sub(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", ' ', input, 0)

        # Remove twitter/instagram handles or any other @ thing
        input = re.sub(r"@([\w\.\_]){1,256}", ' ', input, 0)

        # Remove emojis (taken from https://www.regextester.com/106421)
        input = re.sub(r"(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])", ' ', input, 0)

        # Remove unwanted characters
        input = re.sub(r"[^a-z\ \-\']", ' ', input, 0, re.MULTILINE)

        # Remove multiple spaces
        input = re.sub(r"\ +", ' ', input, 0)

        # Return stripped output
        return input.strip()

    # Running it twice formats everything correctly
    return do(do(input))


# Run validation tests
tests = [
    # ["input", "expected output"]
    ["eVeRyThInG SmAlL", "everything small"],
    ["  no   extra\tspaces  ", "no extra spaces"],
    ["no 12 numbers 423", "no numbers"],
    ["holy @#$%", "holy"],
    ["no p10 characters j3j3 with 100k numbers", "no characters with numbers"],
    ["<html>no tags<html>", "no tags"],
    ["Is 50 <= 100?", "is"],
    ["&amp; no escapes &quo;", "no escapes"],
    ["hypenated-words are okay", "hypenated-words are okay"],
    ["stray -hyphens- - oh - nooo", "stray hyphens oh nooo"],
    ["but m/n dashes—are–not - okay", "but m n dashes are not okay"],
    ["you by harry's  '' ''  '  wife ' ' ' completed", "you by harry's wife completed"],
    ["73K1.8K40 \"𝑰'𝒅 𝒘𝒂𝒍𝒌 𝒕𝒉𝒓𝒐𝒖𝒈𝒉 𝒇𝒊𝒓𝒆 𝒇𝒐𝒓 𝒚'𝒐𝒖, 𝒋𝒖𝒔𝒕 𝒍𝒆'𝒕 𝒎𝒆 test", "test"],
    ["it's a small world", "it's a small world"],
    ["const string = 'test'", "const string test"],
    ["remove 🥳 emojis", "remove emojis"],
    ["twitter @handle", "twitter"],
    ["no domains indigoresearch.xyz", "no domains"],
    ["no full links https://indigoresearch.xyz/", "no full links"],
    ["Currently I have an input box which will detect the URL and parse the data. So right now, I am using: var urlR = /^(?:([A-Za-z]+):)?(\/{0,3})([0-9.\-A-Za-z]+) (?::(\d+))?(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$/; var url= content.match(urlR); The problem is, when I enter a URL like www.google.com, its not working. when I entered http://www.google.com, it is working. I am not very fluent in regular expressions. Can anyone help me?", "currently i have an input box which will detect the url and parse the data so right now i am using var urlr d var url the problem is when i enter a url like its not working when i entered it is working i am not very fluent in regular expressions can anyone help me"],
    ["\"Browse Community Search Write Log in Sign Up Watpad Stories Refine by tag: watpad wattpad love romance fanfiction teenfiction fiction wattys2019 badboy wattys2018 featured lovestory billionaire possessive drama humor watty highschool teen random marriage 1.2K Stories Waiting at the Altar for You by tasha-c#1 Waiting at the Altar for You by Nat 786K29.3K36 Aryel Richards is walking down the aisle every girl dreams of walking down when they're just little girls. Now she's all grown up, and her turn has finally come. She is... Completed teenwattpadteenfiction +7 more My Mafia Man by volleyball238#2 My Mafia Man by volleyball238 1.4M33.2K25 Juliet was just a normal high school girl who was ready for summer. She had all of it planned out. She would spend some time with her friends and her family. That was un... Completed friendshipfamilyyears +14 more A Trade Of Hearts |✔ by thedarkempress2123#3 A Trade Of Hearts |✔ by Tanya Jaiswal 824K22.1K70 \"The ones you love the most have the power to hurt you the most.\" Vanessa Catherine Hudson at twenty-four is more familiar with this statement than she'd like... Completed arrogantjerkchicklit +21 more Waffle Cones (#1) by evethespy#4 Waffle Cones (#1) by уιℓєι 4.7M326K70 \"Hello?\" \"Um, hey?\" \"Wait, you don't sound like my Aunt Kathy.\" \"Unless I was miraculously converted into a member of the opposi... Completed lovefeaturedshortstory +17 more His Blonde Little Secret by sakz15#5 His Blonde Little Secret by Sakz 22.9M988K66 \"Who says people have to find out?\" Brody smirks, taking another step forward. He's so close to me, I can once again see the gold flecks shining in his green e... Completed cuteloveshy +18 more Forced To Leave You **Watty Awards 2013** by WonderGirl123#6 Forced To Leave You **Watty Awards... by Gigi 226K4.8K26 Summary: After having a clash with management, Harry is forced to make a heartbreaking decision of his life: Break-Up with the one girl he loves Brianna, or watch her... Completed onedirectioncoversfamily +121 more How to get to #1 on Wattpad - Hints and Tips by TaranMatharu#7 How to get to #1 on Wattpad - Hint... by Taran Matharu 260K25K12 I managed to get to #1 on Wattpad for Fantasy as well as Adventure in a month and a half. After four months, I had 1 Million reads and a year later I had 5 million. I wo... Completed besthintsranking +10 more Brothers best friend by hm2802#8 Brothers best friend by hm2802 1.1M18K34 Addison Parker, has always despised one boy, Colton Drake, her brothers best friend. Addison lives with her brother and his best friend Colton, Addison and Ryan's parent... overprotectivefictionwattpad +17 more gynecologist | hs by IfYoureReadinggThis#9 gynecologist | hs by brie ! 1.3M19.4K38 \"i mean this in the most non sexual way possible, you're going to have to spread your legs.\" ____________________________ ᴡᴀʀɴɪɴɢ ; multiple sexual mentions... heartbreakliampaynetrending +17 more How To Get Reads, Votes, and Comments - A Guide by KatherineArlene#10 How To Get Reads, Votes, and Comme... by Katherine A. Ganzel 1M61.7K8 How do I get more reads, votes, and comments? If you find yourself asking that question, then I have some answers for you. What can you do to reach out to readers and... Completed writerswattpadguidebook +15 more Adore You [H.S] by xxstyles_lovexx#11 Adore You [H.S] by Harry’s Wife ;) 73K1.8K40 \"𝑰'𝒅 𝒘𝒂𝒍𝒌 𝒕𝒉𝒓𝒐𝒖𝒈𝒉 𝒇𝒊𝒓𝒆 𝒇𝒐𝒓 𝒚𝒐𝒖, 𝒋𝒖𝒔𝒕 𝒍𝒆𝒕 𝒎𝒆 𝒂𝒅𝒐𝒓𝒆 𝒚𝒐𝒖. 𝑳𝒊𝒌𝒆 𝒊𝒕'𝒔 𝒕𝒉𝒆 𝒐𝒏𝒍𝒚 𝒕𝒉𝒊𝒏𝒈 𝑰'𝒍𝒍 𝒆𝒗𝒆𝒓 𝒅𝒐.&qu... trendingromancewattpad +22 more Marcus Mondragon (Manxboy) by Stalking_My_Stalker#12 Marcus Mondragon (Manxboy) by Stalking_My_Stalker 67.7K2.2K19 Micah is an innocent little boy in a body of a seventeen year old, recently orphaned with his mother and father dying in a plane crash. With a ranch to run and stud... mafiababiesinnocent +10 more Memes by actively_inactive#13 Memes by Netflix and Memes 965K33.1K200 Get your daily dose of memes ;) Completed popularwattpadprize14wattpad +10 more Love after Marriage | Completed  by Manya_Eswar#14 Love after Marriage | Completed by Manya 374K34.1K81 ▪▪▪ A Completed ShivIka's Fanfiction ▪▪▪ ▪▪ Yeh Rishta kis mod thak jayegi ▪▪ What would happen when two individuals who don't wish to get married and never believe in t... Completed rikararomanceshivaay +19 more The Bad Boy's Princess by lilmote124#15 The Bad Boy's Princess by your mother 612K12.6K38 {ON HOLD/SLOW UPDATES} #2 in Teen Fiction !!!!! When Sasha Maybourne experiences yet another panic attack, she does the one thing that comes to mind. She runs... Right... badboysashagirl +18 more 14 Nights In Emeliano's Bed  by Emelradine#16 14 Nights In Emeliano's Bed by Rebecca Johnpee🏵️ 11.2M371K49 {COMPLETED} Forced to spend two weeks with a monster like Emeliano Alfredo, Innocent and determined Rebecca Lewis's life, changed for the worse. ⚜⚜ Traveling back to the... Completed ceorudetrouble +19 more Worst Story on Wattpad ✓ by arcticstars#17 Worst Story on Wattpad ✓ by arcticstars 3M179K4 Sick of cliché Wattpad books? Then this isn't the book for you. We take every single over-used plot, character and trope on Wattpad - from player-meets-nerd to my-boyfri... Completed partyhumorhighschool +16 more Pick Up lines  by icecreamlovebrownies#18 Pick Up lines by Lilly❣️ 356K8K200 Some pick up lines that'll make you laugh :) Disclaimer: I did not make all of these. Highest Rank: |#14 in jokes 03.08.18| |#86 in humor 27.05.17| Completed funnyjokesrandom +8 more Supernatural Imagines by TinyAsianEmpress#19 Supernatural Imagines by TinyAsianEmpress 103K2.1K34 Imagines, preferences, one shots and mini series of supernatural characters and their actors. COMPLETED ➖➖➖➖➖➖➖ ➖ ➖➖ Highest ranking: #1 / 26.4K in Requests [25/04/19... Completed piewinchesterfeatured +21 more My Lucky Stars by NNed94#20 My Lucky Stars by NNed 302K6.7K60 Mia Evelyn, 24 years old who owns a small book cafe in New York and leads a happy life with her twin babies. Ryan Zachary Harrison, a 27 years old bachelor and a billio... Completed newadultkindinnocent +10 more Paid StoriesTry PremiumGet the AppLanguageWritersBusinessJobsPressTermsPrivacyHelp© 2020 Wattpad\"", "browse community search write log in sign up watpad stories refine by tag watpad wattpad love romance fanfiction teenfiction fiction badboy featured lovestory billionaire possessive drama humor watty highschool teen random marriage stories waiting at the altar for you by waiting at the altar for you by nat aryel richards is walking down the aisle every girl dreams of walking down when they're just little girls now she's all grown up and her turn has finally come she is completed teenwattpadteenfiction more my mafia man by my mafia man by juliet was just a normal high school girl who was ready for summer she had all of it planned out she would spend some time with her friends and her family that was un completed friendshipfamilyyears more a trade of hearts by a trade of hearts by tanya jaiswal the ones you love the most have the power to hurt you the most vanessa catherine hudson at twenty-four is more familiar with this statement than she'd like completed arrogantjerkchicklit more waffle cones by waffle cones by hello um hey wait you don't sound like my aunt kathy unless i was miraculously converted into a member of the opposi completed lovefeaturedshortstory more his blonde little secret by his blonde little secret by sakz who says people have to find out brody smirks taking another step forward he's so close to me i can once again see the gold flecks shining in his green e completed cuteloveshy more forced to leave you watty awards by forced to leave you watty awards by gigi summary after having a clash with management harry is forced to make a heartbreaking decision of his life break-up with the one girl he loves brianna or watch her completed onedirectioncoversfamily more how to get to on wattpad hints and tips by how to get to on wattpad hint by taran matharu i managed to get to on wattpad for fantasy as well as adventure in a month and a half after four months i had million reads and a year later i had million i wo completed besthintsranking more brothers best friend by brothers best friend by addison parker has always despised one boy colton drake her brothers best friend addison lives with her brother and his best friend colton addison and ryan's parent overprotectivefictionwattpad more gynecologist hs by gynecologist hs by brie i mean this in the most non sexual way possible you're going to have to spread your legs multiple sexual mentions heartbreakliampaynetrending more how to get reads votes and comments a guide by how to get reads votes and comme by katherine a ganzel how do i get more reads votes and comments if you find yourself asking that question then i have some answers for you what can you do to reach out to readers and completed writerswattpadguidebook more adore you by adore you by harry's wife completed more love after marriage completed by love after marriage completed by manya a completed shivika's fanfiction yeh rishta kis mod thak jayegi what would happen when two individuals who don't wish to get married and never believe in t completed rikararomanceshivaay more the bad boy's princess by the bad boy's princess by your mother on hold slow updates in teen fiction when sasha maybourne experiences yet another panic attack she does the one thing that comes to mind she runs right badboysashagirl more nights in emeliano's bed by nights in emeliano's bed by rebecca johnpee completed forced to spend two weeks with a monster like emeliano alfredo innocent and determined rebecca lewis's life changed for the worse traveling back to the completed ceorudetrouble more worst story on wattpad by worst story on wattpad by arcticstars sick of clich wattpad books then this isn't the book for you we take every single over-used plot character and trope on wattpad from player-meets-nerd to my-boyfri completed partyhumorhighschool more pick up lines by pick up lines by lilly some pick up lines that'll make you laugh disclaimer i did not make all of these highest rank in jokes in humor completed funnyjokesrandom more supernatural imagines by supernatural imagines by tinyasianempress imagines preferences one shots and mini series of supernatural characters and their actors completed highest ranking in requests completed piewinchesterfeatured more my lucky stars by my lucky stars by nned mia evelyn years old who owns a small book cafe in new york and leads a happy life with her twin babies ryan zachary harrison a years old bachelor and a billio completed newadultkindinnocent more paid storiestry premiumget the applanguagewritersbusinessjobspresstermsprivacyhelp wattpad"]
]

total_passed = 0
total_tests = len(tests)

for test in tests:
    input = test[0]
    correct = test[1]
    output = clean_string(input)
    passed = output == correct
    passed_text = '\033[92mPASSED\033[0m' if passed else '\033[91mFAILED\033[0m'

    print(f'{passed_text}: "{input}" --> "{output}" == "{correct}"')

    if passed:
        total_passed = total_passed + 1

print(f'\nPassed {total_passed} out of {total_tests}')