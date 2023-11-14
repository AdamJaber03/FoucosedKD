from DataGenerator import DataGenerator

spam_topics = [
    "Phishing Emails",
    "Fake Lottery or Prize Emails",
    "Fake Job Offers",
    "Health and Wellness Scams",
    "Financial Scams",
    "Romance Scams",
    "Urgent Action Required",
    "Fake Invoices or Billing Emails",
    "Malware Distribution",
    "Chain Letters or Pyramid Schemes",
    "Get Rich Quick!",
    "Weight Loss Miracles",
    "Guaranteed Investment Returns",
    "Earn Money from Home",
    "Free Luxury Items",
    "Enlarge Your Anatomy",
    "Pharmaceutical Offers",
    "Cheap Prescription Drugs",
    "Win a Free iPhone",
    "Viagra and Cialis Deals",
    "Meet Singles in Your Area",
    "Hot Stock Picks",
    "Exclusive Limited Time Offer",
    "Eliminate Debt Fast",
    "Mortgage Rates Too Low to Believe",
    "You've Won a Lottery",
    "Inheritance from Unknown Relative",
    "Multi-level Marketing Opportunities",
    "Secret to Eternal Youth",
    "Amazing and Easy Weight Loss",
    "Online Dating Secrets",
    "Unclaimed Funds Waiting for You",
    "IRS Tax Refund Notification",
    "Instant Degrees - No Studying",
    "Eliminate Bad Credit",
    "Miracle Diet Patch",
    "Pre-approved Loan Offers",
    "Work from Home and Make Thousands",
    "Stop Snoring Now!",
    "Get Your Ex Back",
    "Russian Brides Looking for Love",
    "As Seen on Oprah",
    "Meet Celebrities Online",
    "Hot Penny Stocks",
    "Human Growth Hormone Products",
    "Casino and Gambling Deals",
    "Limited Time Offer - Act Now!",
    "Refinance Your Mortgage",
    "Fast and Easy Cash",
    "Be Your Own Boss",
    "No Medical Exam Life Insurance",
    "Discounted Software",
    "Lowest Price for [Popular Product]",
    "Cheap Luxury Watches",
    "Make Money While You Sleep",
    "Free Trial - No Strings Attached",
    "Reverses Aging Process",
    "Meet Hot Singles Tonight",
    "Lost 20 Pounds in 2 Weeks",
    "Earn $1,000 per Day",
    "One Time Investment - Lifetime Income",
    "Eliminate Wrinkles Instantly",
    "Hot Investment Tips",
    "Exotic Vacation Deals",
    "Limited Quantity - Act Fast",
    "Cure for Baldness",
    "Get Out of Debt Now",
    "Serious Cash - No Gimmicks",
    "Special Promotion - Act Immediately",
    "Blast Fat Away",
    "No Credit Check Loans",
    "Double Your Income",
    "Work from Anywhere",
    "Drastically Reduce Cellulite",
    "Best Price Guaranteed",
    "Risk-Free Trial",
    "Never Work Again",
    "Make Money Fast",
    "Bulk Email Marketing",
    "Earn Extra Cash",
    "Rebuild Your Credit",
    "100% Satisfaction Guaranteed",
    "As Seen on TV",
    "Lose Inches Fast",
    "Lower Your Bills",
    "No Questions Asked",
    "Get Paid for Your Opinion",
    "Hot Online Business Opportunities",
    "Boost Your Credit Score",
    "Recession-Proof Income",
    "No Catch - Guaranteed",
    "Alternative Income Sources",
    "Earn Money Overnight",
    "Instant Access",
    "Hot Investment Opportunities",
    "No Hidden Fees",
    "Serious Inquiries Only",
    "While Supplies Last",
    "Money Back Guarantee",
    "Double Your Investment",
    "Lower Your Mortgage Rate",
    "Limited Time Only",
    "Great Offer",
    "Extra Cash",
    "Direct Email Marketing",
    "Increase Sales",
    "Full Refund",
    "This Isn't a Scam",
]

# Check the length of the list
print(len(spam_topics))

ham_topics = [
    "Work-related Correspondence",
    "Personal Communication",
    "Newsletter Subscriptions",
    "Account Notifications",
    "Receipts and Invoices",
    "Social Media Notifications",
    "Updates from Subscribed Services",
    "Online Purchase Confirmations",
    "Event Invitations",
    "Professional Network Invitations",
    "Educational Announcements",
    "Collaboration Requests",
    "Meeting Agendas and Minutes",
    "Customer Support Responses",
    "Travel Itineraries",
    "Subscription Renewal Notices",
    "Product or Service Updates",
    "Feedback and Surveys",
    "Password Reset Requests",
    "Software License Renewals",
    "Legal Document Signatures",
    "Family and Friends Updates",
    "Health Appointment Reminders",
    "Utility Bills and Statements",
    "Government Notices",
    "Bank Statements",
    "Job Application Acknowledgments",
    "Webinar or Workshop Invitations",
    "Open Source Project Discussions",
    "Volunteer Opportunities",
    "Work-related updates",
    "Project status reports",
    "Meeting invitations and follow-ups",
    "Collaboration requests",
    "Webinar invitations",
    "Training announcements",
    "Educational resources and tips",
    "Social events",
    "Networking events",
    "Conference and seminar invitations",
    "Company newsletters",
    "Industry updates",
    "Product announcements",
    "Order confirmations",
    "Shipping updates",
    "Customer support interactions",
    "Birthday and celebration invitations",
    "Personal achievements",
    "General life updates",
    "Charity events",
    "Community service opportunities",
    "Fundraising appeals",
    "Customer satisfaction surveys",
    "Feedback requests",
    "Product improvement surveys",
    "Job openings",
    "Career development opportunities",
    "Networking for career advancement",
    "Fitness challenges",
    "Wellness tips and resources",
    "Health-related events",
    "Investment updates",
    "Financial planning advice",
    "Budgeting tips",
    "Software updates",
    "New product releases",
    "Technology news and tips",
    "Policy updates",
    "Compliance reminders",
    "Legal notices",
    "Travel itineraries",
    "Vacation rental confirmations",
    "Travel tips and recommendations",
    "Green initiatives",
    "Sustainability practices",
    "Environmental awareness campaigns",
    "Family updates",
    "Holiday greetings",
    "Dinner invitations",
    "Recipe sharing",
    "Book recommendations",
    "Movie and TV show suggestions",
    "Music recommendations",
    "Hobby-related discussions",
    "Photography sharing",
    "Gardening tips",
    "Pet-related updates",
    "Home improvement ideas",
    "Local community news",
    "Weather updates",
    "Government announcements",
    "Education-related updates",
    "Graduation invitations",
    "Class reunion announcements",
    "Art and cultural events",
    "Museum exhibitions",
    "Artistic performances",
    "Science and technology advancements",
    "Historical facts and events",
    "Philosophical discussions",
    "Personal finance tips",
    "Home organization tips",
    "Fashion and style updates",
    "DIY project ideas",
    "Job promotions and achievements",
    "Volunteer recognition",
    "Language learning resources",
    "Time management tips",
    "Positive affirmations",
    "Mindfulness and meditation resources",
    "Local business promotions",
    "Discount and sale announcements",
    "Customer loyalty rewards",
    "Community engagement initiatives",
    "Parenting tips and advice",
    "Parent-teacher meeting invitations",
    "Educational webinars for parents",
    "Parenting support groups",
    "Culinary experiences and recommendations",
    "Restaurant reviews",
    "Food and beverage events",
    "Cooking classes",
    "Community sports events",
    "Local sports team updates",
    "Sports and fitness challenges",
    "Sports tournament invitations",
    "Celebration of cultural diversity",
    "Holiday traditions and customs",
    "Travel destination recommendations",
    "Local tourism events",
    "Job fairs and career expos",
    "Professional development workshops",
    "Artisan and craft fairs",
    "Farming and agriculture updates",
    "Local farmers' markets",
    "Community theater performances",
    "Music concerts and festivals",
    "Community health clinics",
    "Health and wellness workshops",
    "Technology and innovation competitions",
    "Community improvement projects",
    "Political town hall meetings",
    "Local government town hall meetings",
    "Neighborhood watch updates",
    "Safety and emergency preparedness tips"
]



if __name__ == "__main__":
    model_desc = "a model that receives an email's body content and outputs a boolean parameter representing weather the email is spam. 0 means not spam (ham) and 1 means spam"
    generator = DataGenerator(
        model_name="spam_detector",
        model_desc=model_desc
    )
#     examples = [{"input": r"""vince ,
# i am going to have the team look at the problem . hopefully it will be an
# easy fix . otherwise , we can work off the worksheets that you complete over
# the weekend . you have my cell number if you have any questions .
# norma villarreal
# 713 - 598 - 1545""",
#                  "output": "0",
#                  "description": "Problem-solving assurance for Vince, support over the weekend"},
#                 {"input": r"""your credit report doesn't matter to us if you own real estate and want immediate ready money to spend any way you like or simply wish to lower your current payments by a third or more here is best deal we can offer you this night hurry this tender will expire today escapenumber escapenumber loan and even more after further review our lenders have established the lowest current payments hurry when best deal is gone it is gone simply finish this quick form don't worry about approval your credit history will not disqualify you http bathaeonand com""",
#                 "output": "1",
#                  "description": "Urgent loan offer with no credit check, act quickly!"},
#                 {"input": r"""hi grant ,
# as requested i have sent a quick summary document giving an up - to - date
# description of the var model .
# i may well have missed some points but cantekin has worked closely with me on
# any changes so it is worth
# consulting him on any details i have missed .
# thanks
# kirstee""",
#                  "output": "0",
#                  "description": "Grant, quick summary of updated VAR model sent as requested."},
#                 # {"input": r"""who are free to come relate to others and a lack of playtime medicine escapenumber for videos enrichment contribute to depression dear customer too much number of men were not pleased with the size of their escapenumber phallus today we suggest you to solve these difficulties without any surgical escapenumber or hormone methods we provide for you absolutely new solution fast extender activity of fast extender based on stretching tissues which escapenumber stimulate regular growth of cells our method escapenumber efficiently and safely and all experts approved only escapenumber this preparation fast extender will act perfectly for every man despite of age escapenumber and business go to website escapenumber and marketing pitches three mornings for many families they must be""",
#                 #  "output": "1",
#                 #  "description": "Boost size without surgery: Fast extender for safe growth."},
#                 # {"input": "yea let's say i constructed a matrix with rownames colnames be those unique elements then what should i do i don't want to do mapply etc to find the field i'm wondering if there's a smarter way using row col etc thanks moshe olshansky escapenumber wrote if your original matrix is a then unique a people and unique a desc will produce a vector of different people and a vector of different descriptions yoooooo wrote hi all let's say i have matrix people desc value mary height escapenumber mary weight escapenumber fanny height escapenumber fanny height escapenumber is there a quick way to form the following matrix people height weight mary escapenumber escapenumber fanny escapenumber escapenumber assuming i don't know the length of people desc and let's say these are characters matrix i tried play with row col etc but i don't seem to find like a duplicate match function i'm trying to write some one two liner that convert my resulting matrix to vector and pick the appropriate fields etc thanks view this message in context http www nabble com restructuring matrix tfescapenumber html aescapenumber sent from the r help mailing list archive at nabble com r help stat math ethz ch mailing list https stat ethz ch mailman listinfo r help please do read the posting guide http www r project org posting guide html and provide commented minimal self contained reproducible code r help stat math ethz ch mailing list https stat ethz ch mailman listinfo r help please do read the posting guide http www r project org posting guide html and provide commented minimal self contained reproducible code view this message in context http www nabble com restructuring matrix tfescapenumber html aescapenumber sent from the r help mailing list archive at nabble com r help stat math ethz ch mailing list https stat ethz ch mailman listinfo r help please do read the posting guide http www r project org posting guide html and provide commented minimal self contained reproducible code",
#                 #  "output": "0",
#                 #  "description": "Seeking efficient matrix restructuring advice in R programming. Help appreciated."},
#                 # {"input": "these people had ideas too their products and others http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank have been featured in the following stores home depot target dick http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blanks sporting goods sears wal mart solutions auto zone fao schwarz sports authority hammacher schlemmer jc penney linens http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blankn things home trends get organized home focus dunham sports modell http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blanks i http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blankve been trying for many years to find an honest company that could represent my product and i just couldn http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blankt find one but when i found davison they were very honest with me i really recommend them they http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blankre really faithful raul from california wine butler get our process started now on your idea click to submit your idea davison provides services to professionally prepare and present product ideas to potential licensees some services are provided for a contingent fee or a percentage of royalties obtained by the client and some services are provided for an upfront fee paid by the client davison does not perform analysis of the potential feasibility marketability patentability or profitability of ideas submitted to it new product development is an uncertain endeavor and davison does not represent or guarantee expressly or impliedly that an idea submitted to it will be licensed sell on any market or provide a positive return to the inventor on money spent for development of the six clients depicted in the pictures above two of the inventors have not realized a net profit on their products one client was a former client and compensated consultant of davison these people had ideas too their products and others http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank have been featured in the following stores home depot target dick http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blanks sporting goods sears wal mart solutions auto zone fao schwarz sports authority hammacher schlemmer jc penney linens http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blankn things home trends get organized home focus dunham sports modell http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blanks i http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blankve been trying for many years to find an honest company that could represent my product and i just couldn http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blankt find one but when i found davison they were very honest with me i really recommend them they http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blank http dailylanedepot com x escapelong escapelong escapelong mtuxmdaescapenumber ng oteescapenumbermg mtiescapenumberotm odqzna html target blankre really faithful raul from california wine butler get our process started now on your idea click to submit your idea davison provides services to professionally prepare and present product ideas to potential licensees some services are provided for a contingent fee or a percentage of royalties obtained by the client and some services are provided for an upfront fee paid by the client davison does not perform analysis of the potential feasibility marketability patentability or profitability of ideas submitted to it new product development is an uncertain endeavor and davison does not represent or guarantee expressly or impliedly that an idea submitted to it will be licensed sell on any market or provide a positive return to the inventor on money spent for development of the six clients depicted in the pictures above two of the inventors have not realized a net profit on their products one client was a former client and compensated consultant of davison",
#                 #  "output": "1",
#                 #  "description": "Product promotion spam with dubious testimonials and false promises."},
#                 {"input": """shirley ,
# please schedule an interview with konstantin on may 8 .
# stinson , zimin , alex , tanya , krishna , myself .
# vince
# - - - - - - - - - - - - - - - - - - - - - - forwarded by vince j kaminski / hou / ect on 05 / 02 / 2001 03 : 07 pm - - - - - - - - - - - - - - - - - - - - - - - - - - -
# " konstantin n . kudin " on 05 / 02 / 2001 01 : 39 : 15 pm
# to :
# cc :
# subject : an interview
# dear dr . kaminski
# we have talked earlier during your energy class at rice about career
# opportunities in risk management at enron . if it is possible , i would like
# to meet with you and people from your group next week , preferably tuesday
# ( may 8 ) . my time is flexible , i could come any time . other days are also
# fine .
# thank you very much in advance .
# sincerely ,
# konstantin kudin""",
#                  "output": "0",
#                  "description": "Interview scheduling request for Konstantin on May 8th. Urgent response needed."},
#                 {"input": "congratulations ! you have been selected to win a free luxury cruise for two to the caribbean ! simply click the link below to claim your prize and book your dream vacation now ! www . luxury-cruise-giveaway . com",
#                  "output": "1",
#                  "description": "Exclusive limited time offer: Win a luxury cruise for two to the Caribbean!"}]
#                                     #{"input": r"""submitting your website in search engines may increase your online sales dramatically .
#                                     # if you invested time and money into your website , you simply must submit your website
#                                     # online otherwise it will be invisible virtually , which means efforts spent in vain . if you want
#                                     # people to know about your website and boost your revenues , the only way to do that is to
#                                     # make your site visible in places where people search for information , i . e . submit your
#                                     # website in multiple search engines .
#                                     # submit your website online and watch visitors stream to your e - business .
#                                     # best regards ,
#                                     # johanna britt""",
#                                     #                  "output": "1"}
    #additional_instructions = f"make sure to create a varied dataset of unique examples, dont repeat examples and create a lot of different unique examples. here is a list of spam email types you should use: {spam_email_headers}. here is a list of non-spam email types you should use: {non_spam_email_headers}"
    examples = [
        {
            "description": "Premium Medication: Easy, Private, and Secure Ordering!",
            "input": """it is difficult to make our material condition better by the best law , but it is easy enough to ruin it by bad laws .
excuse me . . . : ) you just found the
best and simpliest site for
medication on the net . no perscription , easy
delivery .
private , secure , and easy .
better see rightly on a pound a week than squint on a million .
we ` ve got
anything that you will ever want .
erection treatment pills , anti - depressant pills , weight loss , and
more ! http : / / splicings . bombahakcx . com / 3 /
knowledge and human power are synonymous .
only high - quality stuff for low rates !
100 % moneyback guarantee !
there is no god , nature sufficeth unto herself in no wise hath she need of an author .""",
            "output": "1"
        },
        {
            "description": "New Team Member Alert: Molly Magee Joins EOPS Recruiting Team!",
            "input": """i ' m happy to introduce molly magee as the newest addition to the eops
recruiting team . toni and molly have divided their recruiting duties
along separate job functions . please review the information below and
direct your staffing requests to either toni or molly depending on your job
needs .
toni graham - accounting , risk and confirmation / settlements positions ( or
openings requiring a similar skill set of this candidate pool )
molly magee - logistics , global data management , research , legal , competitive
analysis , contract administration and other positions ( or openings requiring
a similar skill set of this candidate pool )
thanks for your assistance ,
hgm""",
            "output": "0"
        },
        {
            "description": "Unbeatable Software Deals: Save Big on Top Products!",
            "input": """microsoft windows xp professioznal 2002
retail price : $ 270 . 99 our low pricie : $ 50 . 00 you save : $ 220 . 00
adobe photoshkop 7 . 0
retail price : $ 609 . 99 our low price : $ 60 . 00 you savue : $ 550 . 00
microsoft office xp professional 2002
retail price : $ 579 . 99 our low price : $ 60 . 00 you savxe : $ 510 . 00
adobe illustrator 10 retaitl price : $ 270 . 99 our low price : $ 60 . 00 you savxe : $ 210 . 00
corel draw graphics suite 11 rehtail price : $ 270 . 99 our low pricje : $ 60 . 00 you save : $ 210 . 00
delphi 7
retaifl price : $ 404 . 99 our low price : $ 60 . 00 you save : $ 335 . 00
and more ! ! !
why so cheap ?
all the software is oem - meaninag that you don ' t get the box and the manual with your software . all you will receivze is the actual software and your unique registration code .
all the softwarue is in the english language for pc . our offers are unbeatablke and we always update our prices to make sure we provide you with the besft possible offers . hurry up and place your ordner , because our supplies are limited .
visimt us now ! http : / / cheap - drugs - here . biz / oeol 7 / ? affiliate _ id = 233763 & campaign _ id = 601
fwunrt fmooetr ltby nyqkgbphb krgzgl vbbmigb zwftnqlp oaohkv icckmv rmcetdf wmlx lidfxvrnk tdrezc hbmvxft zjqdpnpd ldloti jbywub ozaqgcf czjj yvcbkprnc vbrekd fizzjnz kgfmkhmw rkqumd kgrnbt ggejkmi kyyj jepyoyklp wekjhw pajrtqy ybjlkvjj gvnwte ueqjbv vkcrccd uwut uwdhtzrrf mhbglw jdhkydx bvaeyvat nvorcx qvpwtx yniuzlb kkei lziqyfqqu mhlped kuauryt bthnutaz clzkex pvojiw xaablvb gnao otxenpenr qmdvju qafbwcc xdntfvhf jxzhbn
""",
            "output": "1"
        },
        {
            "description": "Attachment: hplnol26.xls - Please Review",
            "input": """( see attached file : hplnol 26 . xls )
- hplnol 26 . xls""",
            "output": "0"
        },
        {"description": "Grand Opening: Dive into Ocean Treasure Online Casino! ",
            "input": """grand opening - ocean treasure online casino .
enjoy real casino action on your desktop with these
exciting promotional offers :
get $ 300 bonus on your first deposit !
enter this code in the casino software ' s cashier : x 3 daw
get $ 10 free , no deposit needed ! enter this code : frlee
allow us to show you our quality operation , fast payouts ,
generous bonuses , and super friendly around - the - clock
customer support .
go here : http : / / otcasino . biz
best regards ,
steven hughes
no thanks : http : / / otcasino . biz / u /
""",
            "output": "1"},
        {
            "description": "Important Update: Imbalances Report - Please Review",
            "input": """. . . . this just in . . . .
here are our updated imbalances per contract & total :
historical current mth cumul .
201 k : ( 12 . 807 ) ( 8 . 181 ) ( 20 . 988 )
202 k : ( 13 . 951 ) 7 . 879 ( 6 . 072 )
203 k : ( 6 . 152 ) ( 267 ) ( 6 . 419 )
204 k : 27 . 392 ( 6 . 306 ) 21 . 088
total : ( 5 . 516 ) ( 6 . 875 ) ( 12 . 391 )
due oasis""",
            "output": "0"
        }
    ]
    additional_instructions = f"make sure to generate new unique and random examples, the spam emails should be realistic and blivble, dont repeat examples and dont generate the most obvious and simple example. make sure to create both complex and long emails and simple and short emails. try ro make the emails as realistic as possible as the model we are training will be evaluated on real world data, so be as concrete as possible, use made up names numbers and links like steven, ashly, 8500$, december 2nd, www.somelink.com, www.paypal.com...\n here s a list of general spam email topics use many them randomly and mix around: {spam_topics}\nhere is a list general topics for of non spam (ham) emails use many them randomly and mix around: {ham_topics}"
    df = generator.generate_dataset(1000, additional_instructions=additional_instructions, examples=examples)
    print("haaaalllloooooo")