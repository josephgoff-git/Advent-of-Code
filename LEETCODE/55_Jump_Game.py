class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True
    
sol = Solution()
print(sol.canJump([2,3,1,1,4]))

list = """align-content
align-items
align-self
animation
animation-delay
animation-direction
animation-duration
animation-fill-mode
animation-iteration-count
animation-name
animation-play-state
animation-timing-function
backface-visibility
background
background-attachment
background-clip
background-color
background-image
background-origin
background-position
background-repeat
background-size
border
border-bottom
border-bottom-color
border-bottom-left-radius
border-bottom-right-radius
border-bottom-style
border-bottom-width
border-collapse
border-color
border-image
border-image-outset
border-image-repeat
border-image-slice
border-image-source
border-image-width
border-left
border-left-color
border-left-style
border-left-width
border-radius
border-right
border-right-color
border-right-style
border-right-width
border-spacing
border-style
border-top
border-top-color
border-top-left-radius
border-top-right-radius
border-top-style
border-top-width
border-width
bottom
box-shadow
box-sizing
caption-side
clear
clip
color
column-count
column-fill
column-gap
column-rule
column-rule-color
column-rule-style
column-rule-width
column-span
column-width
columns
content
counter-increment
counter-reset
cursor
direction
display
empty-cells
flex
flex-basis
flex-direction
flex-flow
flex-grow
flex-shrink
flex-wrap
float
font
font-family
font-size
font-size-adjust
font-stretch
font-style
font-variant
font-weight
height
justify-content
left
letter-spacing
line-height
list-style
list-style-image
list-style-position
list-style-type
margin
margin-bottom
margin-left
margin-right
margin-top
max-height
max-width
min-height
min-width
opacity
order
outline
outline-color
outline-offset
outline-style
outline-width
overflow
overflow-x
overflow-y
padding
padding-bottom
padding-left
padding-right
padding-top
page-break-after
page-break-before
page-break-inside
perspective
perspective-origin
position
quotes
resize
right
tab-size
table-layout
text-align
text-align-last
text-decoration
text-decoration-color
text-decoration-line
text-decoration-style
text-indent
text-justify
text-overflow
text-shadow
text-transform
top
transform
transform-origin
transform-style
transition
transition-delay
transition-duration
transition-property
transition-timing-function
vertical-align
visibility
white-space
width
word-break
word-spacing
word-wrap
z-index"""

list2 = list.split("\n")
print(list2)


contacts = """ASUS
ASUS 
ASUS 
Better Help
Better Help
Better Help
Athletic Greens
Athletic Greens
Athletic Greens
QuickBooks
QuickBooks
Little Caesar Enterprises
Little Caesar Enterprises
Little Caesar Enterprises
ExpressVPN
ExpressVPN
Brilliant
Brilliant
Shopify
Shopify
Shopify
Shopify
Meliopayments
Meliopayments
Capital One Financial
Capital One Financial
Acorns
Acorns
HBO
HBO
McDonald's
McDonald's
ZipRecruiter
ZipRecruiter
Squarespace
Squarespace
Squarespace
Discord
Discord
Discord
Paramount Animation
Paramount Animation
Skillshare
Skillshare
Skillshare 
Audible
Audible
Audible
Dollar Shave Club
Dollar Shave Club
Postmates
Postmates
Seatgeek
Seatgeek
HelloFresh
HelloFresh
Grammarly
Oculus VR
Oculus VR
Oculus VR
Nord VPN
Nord VPN
Altium
Altium
Altium
FORT Robotics
FORT Robotics 
Storyblocks
Storyblocks
Storyblocks
Squarespace
Squarespace
Hotels.com 
Hotels.com 
Halo Top
GNC
GNC
Headspace
Headspace
Digi-Key Electronics
Digi-Key Electronics
Digi-Key Electronics
DJI (China)
DJI (China)
DJI (China)
DJI (China)
DJI (China)
DJI (China)
KiwiCo
KiwiCo
KiwiCo
Wix
Wix
Wix
Wix
Gymshark
Gymshark
Gymshark
Red Bull
Red Bull
Red Bull
Red Bull
Monster
Monster 
Monster
Monster
Skillshare
Skillshare
Skillshare
Skillshare
Bose
Bose
Audible
Audible
Audible
Audible
Audible
Micro Center
Micro Center
Micro Center
Micro Center
Bark
Bark
Framebridge
Framebridge
Hubble Contacts
Hubble Contacts
Cash App
Cash App
Cash App
Cash App
Mubi
Mubi
GoDaddy
GoDaddy
GoDaddy
Robinhood
Robinhood
Peloton
Peloton
Fiverr
Fiverr
Fiverr
Fiverr
Fiverr
Fiverr
Freshbooks
Freshbooks
Freshbooks
Curiosity Stream
Curiosity Stream
Curiosity Stream
Gorilla Glue
Gorilla Glue
MakerBot
MakerBot
Wondrium
Wondrium
Wondrium
SYIL
Rings Central 
Rings Central 
Grammarly
Grammarly 
Grammarly 
OnePlus
OnePlus
OnePlus
Glassdoor
Glassdoor
Glassdoor
Microsoft
Microsoft
Microsoft
Microsoft
PayPal
PayPal
PayPal (Honey)
Handshake
Handshake
Handshake
A24
A24
A24
Private Internet Access
Private Internet Access
Draft Kings
Draft Kings 
Draft Kings 
Fox Bet
Fox Bet
6am City
6am City
6am City
6am City
Fractal Design
Hubspot
Hubspot
Hubspot
MSI
MSI
Nvidia 
Nvidia 
Nvidia 
Nvidia 
Corsair
Corsair
Corsair
AData
AData
Adata
NGINX
NGINX
Zapier
Zapier
Shopgld
Shopgld
Honor
Honor
Honor
Honor
Honey
Babbel
Babbel
Turbo Tax
Turbo tax
Lenovo
Lenovo
Lenovo
Nreal
Nreal
Anker Technology
Anker Technology
Canon
Canon
Canon
Insta360
Insta360
Insta360
Chipotle
Chipotle
Chipotle
Netflix
Netflix
Netflix
Calvin Klein
Calvin Klein
Calvin Klein
ClickUp
ClickUp
ClickUp
ClickUp
SEMrush
SEMrush
SEMrush
SEMrush
SEMrush
GoPro
GoPro
GoPro
GoPro
Formlabs
Formlabs
Formlabs
SolidWorks
SolidWorks
SolidWorks
Crocs
Crocs
Crocs
Crocs
Scopely
Scopely
Scopely
Scopely
PCBWay
PCBWay
Onshape
Onshape
Onshape
Notion
Notion
Notion
Spirit Airlines
Spirit Airlines
Spirit Airlines
PetSmart
PetSmart
PetSmart
PetSmart
PetSmart
Ugreen Group
Ugreen Group
Ugreen Group
Ugreen Group
Valve Corporation
Valve Corporation
Valve Corporation
Hulu
Hulu
Hulu
Hulu
Etsy
Etsy
Etsy
Etsy
Etsy
Revolut
Revolut
Revolut
Revolut
Revolut
AirBnB
AirBnB
AirBnB
AirBnB
Paramount
Paramount
Paramount
Paramount
Shippo
Shippo
Shippo
Shippo
ShipStation
ShipStation
ShipStation
Curology
Curology
Curology
Curology
Curology
Adobe
Adobe
Adobe
Adobe
Audio-Technica
Audio-Technica
Audio-Technica
Audio-Technica
Dell
Dell
Dell
Dell
Dell
AMD
AMD
AMD
Fabletics
Fabletics
Fabletics
Fabletics
Fabletics
Away
Away
Away
Away
Away
Allbirds
Allbirds
Allbirds
Allbirds
Mejuri
Mejuri
Mejuri
Mejuri
Dr. Squatch
Dr. Squatch
Dr. Squatch
Dr. Squatch
Synology
Synology
Synology
Synology
Synology
Epic Games
Epic Games
Epic Games
Epic Games
SoFi
SoFi
SoFi
CarParts.com
CarParts.com
CarParts.com
CarParts.com
Zoho
Zoho
Zoho
Zoho
Razer
Razer
Razer
Razer
RingCentral
RingCentral
RingCentral
Hootsuite
Hootsuite
Hootsuite
Hootsuite
Wacom
Wacom
Wacom
Wacom
Blue Apron
Blue Apron
Blue Apron
Blue Apron
23andme
23andme
23andme
23andme
Casper
Casper
Casper
Casper
Gorgias
Gorgias
Gorgias
Dashlane
Dashlane
Dashlane
Dashlane
AnyDesk
AnyDesk
AnyDesk
Backblaze
Backblaze
Backblaze
Zotac
Zotac
Zotac
iFixit
iFixit
Adorama
Adorama
Adorama
Adorama
Bark Parental Controls
Bark Parental Controls
Best Buy
Best Buy
Best Buy
Best Buy
Belkin
Belkin
Belkin
eBay
eBay
eBay
eBay
Epidemic Sound
Epidemic Sound
Epomaker
EyeBuyDirect
EyeBuyDirect
GoTo
GoTo
GoTo
GoTo
JumpCloud
JumpCloud
JumpCloud
Linode
Linode
Magic Spoon
Magic Spoon
Magic Spoon
Manscaped
Manscaped
Manscaped
Newegg
Newegg
Newegg
Depop
Depop
Depop
Nothing Tech
Nothing Tech
Ourplace
Ourplace
OVOU
OVOU
Roland
Roland
Roland
Shutterstock
Shutterstock
Shutterstock
Shutterstock
Shutterstock
Snooz
Snooz
Telus
Telus
Telus
Telus
Unbounce
Unbounce
Unbounce
Vention
Vention
VistaPrint
VistaPrint
VistaPrint
VistaPrint
Western Digital
Western Digital
Western Digital
Western Digital
Western Digital
Eight Sleep
Eight Sleep
Eight Sleep
Gameloft
Gameloft
Gameloft
Gameloft
HCL Technologies
HCL Technologies
HCL Technologies
HCL Technologies
Origin PC
Origin PC
Intel
Intel
Intel
Intel
Intel
Gigabyte Global
Gigabyte Global
Gigabyte Global
Gigabyte Global
Raise3D
Raise3D
Raise3D
Goliath Technologies
Goliath Technologies
Bitdefender
Bitdefender
Bitdefender
Bitdefender
Bitdefender
EKWB
EKWB
Harman
Harman
Harman
Harman
Skullcandy
Skullcandy
Skullcandy
Skullcandy
Thermaltake Technology
Thermaltake Technology
Thermaltake Technology
Thermaltake Technology
Lucid
Lucid
Lucid
Lucid
HP
HP
HP
HP
Alibaba.com
Alibaba.com
Alibaba.com
Alibaba.com
Ocrolus
Ocrolus
Ocrolus
Ocrolus
Universal Audio
Universal Audio
Universal Audio
Universal Audio
Sennheiser Electronics
Sennheiser Electronics
Sennheiser Electronics
Sennheiser Electronics
Rivian
Rivian
Rivian
Huawei
Huawei
Huawei
Huawei
OPPO
OPPO
OPPO
OPPO
Yamaha
Yamaha
Yamaha
Yamaha
Auralex Acoustics
Auralex Acoustics
Auralex Acoustics
Realme
Realme
Motorola
Motorola
Xiomi
Xiomi
Xiomi
Xiomi
Lucid Motors
Lucid Motors
Lucid Motors
Lucid Motors
Seagate
Seagate
Seagate
Roborock
Roborock
Roborock
Roborock
Oura Ring
Oura Ring
Oura Ring
Dropbox
Dropbox
Dropbox
Dropbox
Native Union
Native Union
Native Union
RØDE Microphones
RØDE Microphones
RØDE Microphones
Incipio
Incipio
Scosche Industries
Scosche Industries
Scosche Industries
SteelSeries ApS
SteelSeries ApS
SteelSeries ApS
SteelSeries ApS
Tovala
Tovala
Tovala
Scuf Gaming International
Scuf Gaming International
Scuf Gaming International
Scuf Gaming International
SPIGEN
SPIGEN
SPIGEN
SPIGEN
Output
Output
Apogee Electronics
Apogee Electronics
Shure
Shure
Shure
Shure
Elgato
Elgato
Elgato
Elgato
Sweetwater
Sweetwater
Sweetwater
Maingear
Maingear
Klipsch Group
Klipsch Group
Klipsch Group
Klipsch Group
Snap One
Snap One
Snap One
Snap One
Pioneer Electronics USA
Pioneer Electronics USA
Pioneer Electronics USA
Pioneer Electronics USA
Vivo
Vivo
iQOO Communication Technology
iQOO Communication Technology
iQOO Communication Technology
iQOO Communication Technology
Shokz
Shokz
Shokz
Gel Blaster
Gel Blaster
Gel Blaster
Gel Blaster
Gel Blaster
EcoFlow
EcoFlow
EcoFlow
EcoFlow
Ekster
Ekster
Ekster
MSI
MSI
MSI
MSI
Ecovacs
Ecovacs
Ecovacs
Ecovacs
Garmin
Garmin
Garmin
Garmin
Wish
Wish
Wish
Wish
IK Multimedia
IK Multimedia
IKEA
IKEA
IKEA
IKEA
TP-Link
TP-Link
TP-Link
TP-Link
Atomos
Atomos
Timekettle
Timekettle
Geneverse
Geneverse
Geneverse
Nokia
Nokia
Nokia
NETGEAR
NETGEAR
NETGEAR
MasterWorks
MasterWorks
MasterWorks
MasterWorks
Acer
Acer
Acer
Acer
Ugreen 
Ugreen 
Ugreen 
Adorama
Adorama
Adorama 
Adorama
Best Buy
Best Buy
Best Buy 
Shady Rays
Shady Rays
OMTech Laser
OMTech Laser
Frame.io
Varla Scooter
Chugbud
ToolGuyd
Dewalt
Cuts Clothing 
Cuts Clothing 
Cuts Clothing 
Chewy
Chewy
Salt and Stone
Colgate
Colgate
Colgate
Ring
Ring
Ring
Nordstrom
Nordstrom
Nordstrom
Coco Delivery
Coco Delivery
Bonobos
Bonobos
Bonobos
Bonobos
Burt's Bees
Burt's Bees
Carvana
Carvana
Carvana
OpenDoor
OpenDoor
OpenDoor
Gametime
Gametime
Gametime
Aeropostale
Aeropostale
Aeropostale
Purina
Purina
Purina
Little Caesars
Little Caesars
Little Caesars
Greenix
Brightech
Cameo
Cameo
Cameo
BFGoodrich
BFGoodrich
Malbon Golf
Malbon Golf
Malbon Golf
Jersey Mike's Subs
Jersey Mike's Subs
Jersey Mike's Subs
BetterHelp
BetterHelp
BetterHelp
BetterHelp
TickPick
TickPick
TickPick
Booking.com
Booking.com
Booking.com
5-hour Energy
5-hour Energy
5-hour Energy
Sports Illustrated
Sports Illustrated
Sports Illustrated
Blue Diamond
Blue Diamond
Blue Diamond
Apartments.com
Apartments.com
Apartments.com
Zillow
Tylenol
Clif Bar
Clif Bar
Clif Bar
Universal Technical Institute
Universal Technical Institute
Universal Technical Institute
Dior
Dior
Dior
Panera Bread
Panera Bread
Panera Bread
L'Oreal
L'Oreal
L'Oreal
DripDrop
DripDrop
DripDrop
Hippeas
Hippeas
Hippeas
Carnival
Carnival
Carnival
Jimmy Dean
Sargento
Sargento
Sargento
Ebay
Ebay
Ebay
Ebay
Tropical Smoothie Cafe
Tropical Smoothie Cafe
Tropical Smoothie Cafe
Hefty
Athletic Greens
Athletic Greens
Athletic Greens
Bai
Bai
EcoLab
EcoLab
EcoLab
Wild Fork
Wild Fork
Wild Fork
Hidden Valley
Door Dash
Door Dash
Door Dash
Banana Republic
Banana Republic
Banana Republic
Dave & Buster's
Dave & Buster's
Dave & Buster's
Folgers
Dairy Queen
Dairy Queen
Dairy Queen
Provia
Provia
Provia
Scott's 
Scott's 
Scott's 
Scott's 
Trip Advisor
Trip Advisor
Trip Advisor
Blue Bunny
Blue Bunny
Advance Auto Parts
Advance Auto Parts
Advance Auto Parts
Duluth Trading Co.
Duluth Trading Co.
Duluth Trading Co.
Kayak
Kayak
Kayak
Milwaukee Tool
Milwaukee Tool
Milwaukee Tool
GrubHub
GrubHub
GrubHub
Bare Performance Nutrition
Noom
Noom
Noom
Zoom
Zoom
Zoom
PrizePicks
PrizePicks
PrizePicks
Top Golf
Top Golf
Top Golf
Genesis
Genesis
Genesis
Audible
Audible
Audible
Rad Power Bikes
Rad Power Bikes
Rad Power Bikes
Peloton
Peloton
Peloton
Cymbiotika
Cymbiotika
Cymbiotika
Indeed
Indeed
Indeed
Hilton
Hilton
Hilton
Kelley Blue Book
Kelley Blue Book
Kelley Blue Book
BYLT
BYLT
BYLT
Bumble
Bumble
Bumble
Trojan
Jack in the Box
Jack in the Box
Jack in the Box
SC Johnson
SC Johnson
SC Johnson
Rockstar Energy
Rockstar Energy
Rockstar Energy
Rockstar Games
Rockstar Games
Rockstar Games
Orkin
Orkin
Orkin
Clorox
Clorox
Clorox
Coffee Mate
Coffee Mate
Coffee Mate
M & M's
M & M's
Visible
Visible
Visible
Energizer
Energizer
Energizer
Energizer
Vans
Vans
Vans
Vans
What Do You Meme?
What Do You Meme?
What Do You Meme?
Build-a-Bear
Build-a-Bear
Build-a-Bear
air up
air up
Rakuten
Rakuten
Rakuten
Rakuten
Lululemon
Lululemon
Lululemon
Lululemon
Dyson
Dyson
Dyson
Gold's Gym
Gold's Gym
Gold's Gym
Lyko
Sonic
Sonic
Sonic
Sonic
Roblox
Roblox
Roblox
Roblox
LEGO
LEGO
LEGO
Doritos
Liquid Death
Liquid Death
Liquid Death
Liquid Death
Jack Daniels
Jack Daniels
Jack Daniels
PSD Underwear
PSD Underwear
PSD Underwear
Noodles & Company
Noodles & Company
Noodles & Company
Hasbro
Hasbro
Hasbro
Klarna
Klarna
Klarna
Sephora
Sephora
Sephora
Sephora
Uber 
Uber 
Uber 
Uber 
Flex Seal
Flex Seal
Flex Seal
Rain Guard
Rust-Oleum
Rust-Oleum
Rust-Oleum
Ford
Ford
Ford
Ford
Mattel Games
Mattel Games
Mattel Games
King's Hawaiian
King's Hawaiian
King's Hawaiian
King's Hawaiian
Fitbit
Fitbit
Fitbit
Fitbit
Garmin
Garmin
Garmin
Stem
Stem
Stem
Charles Schwab
Charles Schwab
Charles Schwab
Blendtec
Blendtec
Blendtec
Jala
Roshambo Baby
Infinity Strap
American Express
American Express
American Express
American Express
Intuit
Intuit
Intuit
VRBO
VRBO
VRBO
Slack
Slack
Slack
WhatsApp
WhatsApp
WhatsApp
GoPro
GoPro
GoPro
Spotify
Spotify
Spotify
Wendy's
Wendy's
Wendy's
Hershey's
Hershey's
Hershey's
ASICS
ASICS
ASICS
Panda Express
Panda Express
Panda Express
Warby Parker
Warby Parker
Warby Parker
National Geographic
National Geographic
National Geographic
BarkBox
BarkBox
BarkBox
Wayfair
Wayfair
Wayfair
Heineken
Heineken
Heineken
Turo
Turo
Turo
Turo
KFC
KFC
KFC
KFC
Gamestop
Gamestop
Gamestop
BetterHelp
BetterHelp
BetterHelp
Crunch Base
Crunch Base
Crunch Base
Supertails
Rover.com
Rover.com
Rover.com
Rover.com
Bic
Bic
Bic
Bic
Tinder
Tinder
Tinder
Nutro
Pavilions
Pavilions
Pavilions
FTD.com
FTD.com
FTD.com
FTD.com
My Fitness Pal
My Fitness Pal
My Fitness Pal
Whoop
Whoop
Whoop
Lyft
Lyft
Lyft
Bass Pro Shops
Bass Pro Shops
Bass Pro Shops
Bass Pro Shops
PetSafe
PetSafe
PetSafe
Bee Mortgage
Fashion Nova
Fashion Nova
Fashion Nova
Goli Gummy
Goli Gummy
Goli Gummy
Quest Nutrition
Quest Nutrition
Quest Nutrition
Tesla
Tesla
Tesla
Minecraft
Banish
Banish
Crayola
Crayola
Crayola
Honey
Honey
Honey
GOAT
GOAT
GOAT
Gfuel
Gfuel
Gfuel
PUBG
PUBG
Lootcrate
Lootcrate
Lootcrate
Razer
Razer
Razer
Trello
Trello
Trello
Quidd
Paw.com
Paw.com
Paw.com
Hemper
Hemper
Minted
Minted
Minted
Welly
Welly
Welly
Otterbox
Otterbox
Otterbox
MUD/WTR
MUD/WTR
MUD/WTR
ClickBank
ClickBank
Wrapify
Wrapify
Wrapify
Dollar Tree
Dollar Tree
Dollar Tree
Capri Sun
Sports Clips
Sports Clips
Sports Clips
Bearbottom
Cotopaxi
Cotopaxi
Cotopaxi
Factor75
Chuck E. Cheese
Chuck E. Cheese
Chuck E. Cheese
Terminix
Terminix
Terminix
Greenix
Sargento
Sargento
Sargento
RXBAR
RXBAR
Grenade
MyProtein
MyProtein
Malbon Golf
Hello Tushy
Hello Tushy
Hello Tushy
Dude Products
Dude Products
Dude Products
Secret Lab
UNRL
UNRL
UNRL
Skillshare
Skillshare
Skillshare
Movavi
Movavi
Movavi
Kellogg's
Kellogg's
Kellogg's
BILT
BILT
BILT
Zevia Energy
Zevia Energy
Zevia Energy
5 Hour Energy
5 Hour Energy
5 Hour Energy
Zipfizz
Zipfizz
Zipfizz
Death Wish Coffee
Death Wish Coffee
Death Wish Coffee
Converse
Converse
Converse
CTRL
CTRL
Bulk
Muscle Pharm
Philips
Philips
Philips
Sephora
Sephora
Sephora
Sephora
AdvoCare
AdvoCare
AdvoCare
MGM Resorts
MGM Resorts
MGM Resorts
MGM Resorts
Panasonic
Panasonic
Panasonic
Underdog Fantasy Sports
Underdog Fantasy Sports
Underdog Fantasy Sports
Fanduel
Fanduel
Fanduel
Fanduel
Thursday Boots
Thursday Boots
Thursday Boots
Timberland
Timberland
Timberland
Timberland
Expedia Group
Expedia Group
Expedia Group
Expedia Group
Orbitz
Orbitz
Orbitz
Hotwire
Hotwire
Agoda
Agoda
Agoda
Agoda
Pedigree
Applebee's
Applebee's
Applebee's
Applebee's
Chili's
Chili's
Chili's
Chili's
Patreon
Patreon
Patreon
Patreon
Crest
Sitka Gear
Sitka Gear
Sitka Gear
Sitka Gear
Ducks Unlimited Inc.
Ducks Unlimited Inc.
Kuiu
Kuiu
Kuiu
Kuiu
Drake Waterfowl
Drake Waterfowl
Drake Waterfowl
Canada Goose
Canada Goose
Canada Goose
Canada Goose
Browning
Browning
Browning
Nomad
Nomad
Buck Knives
Buck Knives
Benchmade
Benchmade
Benchmade
Benchmade
Hammer Made
Hammer Made
Hammer Made
Maple Holistics
Maple Holistics
Humm
Humm
Humm
Ray-Ban
Shady Rays
Shady Rays
Shady Rays
Shady Rays
ROKA
ROKA
ROKA
ROKA
SC Johnson
SC Johnson
SC Johnson
SC Johnson
Motorola
Motorola
Motorola
Motorola
Visible
Visible
Visible
Visible
AMPM
Viator Travel
Viator Travel
Viator Travel
Viator Travel
DOT'S
DOT'S
DOT'S
American Eagle
American Eagle
American Eagle
American Eagle
American Eagle
Hulah
Eventbrite
Eventbrite
Eventbrite
Eventbrite
Vuori Clothing
Vuori Clothing
Vuori Clothing
Vuori Clothing
Neutrogena
Neutrogena
Neutrogena
Neutrogena
Airtasker
Airtasker
Airtasker
Airtasker
Nature Valley
Dymatize
Dymatize
Dymatize
Rite Aid
Rite Aid
Rite Aid
Rite Aid
Psycho Bunny
Psycho Bunny
Psycho Bunny
Psycho Bunny
Glossier
Glossier
Glossier
Glossier
Kate Spade
Kate Spade
Kate Spade
Kate Spade
Adidas
Adidas
Adidas
Adidas
ASOS
Daniel Wellington
Daniel Wellington
Daniel Wellington
Daniel Wellington
La Croix
La Croix
La Croix
La Croix
Sperry
Sperry
Sperry
Sperry
Huel
Goli
Goli
Goli
Goli
Amazon Fashion
Amazon Fashion
Amazon Fashion
Amazon Fashion
Everence
Everence
Everence
Everence
MegaFood
MegaFood
MegaFood
MegaFood
Subaru
Subaru
Subaru
Subaru
Frank Body
Frank Body
Frank Body
Urban Outfitters
Urban Outfitters
Urban Outfitters
Urban Outfitters
Nivea
Hello Fresh
Hello Fresh
Hello Fresh
Hello Fresh
Fidelity
Fidelity
Fidelity
Fidelity
Geico
Geico
Geico
Geico
Cars.com
Cars.com
Cars.com
Cars.com
Technogym
Technogym
Technogym
Technogym
Experian
Experian
Experian
Experian
Chanel
Chanel
Chanel
Chanel
Whole Foods Market
Whole Foods Market
Whole Foods Market
Whole Foods Market
Nature Made
Nature Made
Petco
Petco
Petco
Petco
Shipt
Shipt
Shipt
PeoplePerHour
PeoplePerHour
PeoplePerHour
Envato
Envato
Envato
99designs
99designs
99designs
99designs
Liquid IV
Liquid IV
Liquid IV
Liquid IV
Nuun
Nuun
Nuun
Nuun
Propel
Titleist
Coleman
Coleman
Coleman
Coleman
No Cow
No Cow
No Cow
No Cow
Perrier
Instacart
Instacart
Instacart
Instacart
goPuff
goPuff
goPuff
goPuff
goPuff
Pet Smart
Pet Smart
Pet Smart
Pet Smart
Choice Hotels
Choice Hotels
Choice Hotels
Choice Hotels
Choice Hotels
Choice Hotels
Tubi
Tubi
Tubi
Tubi
Tubi
Hims
Hims
Hims
Hims
New Era
New Era
New Era
New Era
Rhone
Rhone
Rhone
Rhone
Catan
Catan
Clinique
Clinique
Clinique
Clinique
Clinique
US Bank
US Bank
US Bank
US Bank
US Bank
Goodyear
Goodyear
Goodyear
Arby's
Arby's
Arby's
Bridgestone
Bridgestone
Target
Target
Target
Target
Target
Blue Bell
Blue Bell
Chevron
Chevron
Chevron
Chevron
Carhartt
Carhartt
Carhartt
Big 5 Sporting Goods
Big 5 Sporting Goods
Big 5 Sporting Goods
Big 5 Sporting Goods
Big 5 Sporting Goods
Wrangler Jeans
Wrangler Jeans
Wrangler Jeans
Wrangler Jeans
Patagonia
Patagonia
Patagonia
Patagonia
Patagonia
Levi Strauss
Levi Strauss
Levi Strauss
Levi Strauss
Levi Strauss
Columbia
Columbia
Columbia
Columbia
The North Face
The North Face
The North Face
The North Face
Turtle Beach
Turtle Beach
Turtle Beach
Turtle Beach
Humble Bundle
Humble Bundle
Humble Bundle
Humble Bundle
Teachable
Teachable
Teachable
Teachable
Radisson
Radisson
Impossible Foods
Impossible Foods
Impossible Foods
Ralph's
Ralph's
Hollister Co.
Hollister Co.
Hollister Co.
Tiqets
Tiqets
GetYourGuide
GetYourGuide
GetYourGuide
GetYourGuide
Headout
Headout
Headout
Headout
Fiat
Fiat
Crunch Fitness
Crunch Fitness
Crunch Fitness
Crunch Fitness
Planet Fitness
Planet Fitness
Planet Fitness
Planet Fitness
Equinox
Equinox
Equinox
Equinox
Qdoba
Qdoba
Qdoba
Qdoba
Jimmy John's
Jimmy John's
Jimmy John's
Jimmy John's
Subway
Subway
Subway
Subway
Gatorade
Gatorade
Gatorade
Frito Lay
Frito Lay
Frito Lay
Frito Lay
Frito Lay
ExpressVPN
ExpressVPN
ExpressVPN
ExpressVPN
Squarespace
Squarespace
Squarespace
Squarespace
Squarespace
Magic Spoon
Magic Spoon
Magic Spoon
Magic Spoon
Magic Spoon
Fetch Rewards
Fetch Rewards
Fetch Rewards
Fetch Rewards
Fetch Rewards
Fetch Rewards
Surfshark
Surfshark
Function of Beauty
Function of Beauty
Function of Beauty
Function of Beauty
The Ridge Wallet
The Ridge Wallet
The Ridge Wallet
The Ridge Wallet
Helix Sleep
Helix Sleep
Helix Sleep
Bokksu
Dunkin' Donuts
Dunkin' Donuts
Dunkin' Donuts
Dunkin' Donuts
Taco Bell
Taco Bell
Taco Bell
Taco Bell
Idahoan Foods
Idahoan Foods
Idahoan Foods
Idahoan Foods
F'Real
F'Real
F'Real
Ralph Lauren
Ralph Lauren
Ralph Lauren
Ralph Lauren
Abercrombie & Fitch
Abercrombie & Fitch
Abercrombie & Fitch
Abercrombie & Fitch
Calvin Klein
Calvin Klein
Calvin Klein
Calvin Klein
PacSun
PacSun
PacSun
PacSun
PacSun
Revolve
Revolve
Revolve
Revolve
Revolve
Supreme
Supreme
Supreme
Pepsi
Pepsi
Pepsi
Doritos
Chevrolet
Chevrolet
Chevrolet
Chevrolet
CapitalOne
CapitalOne
CapitalOne
CapitalOne
CapitalOne
Discover
Discover
Discover
Calm App
Calm App
Calm App
ALO
ALO
ALO
ALO
ALO
Vuori
Vuori
Vuori
Vuori
Men's Health
Men's Health
Under Armour
Under Armour
Under Armour
Under Armour
Under Armour
Athleta
Athleta
Athleta
Athleta
Peacock
Peacock
Peacock
Peacock
Got2B
American Crew
Garden of Life
Garden of Life
Garden of Life
Garden of Life
Sun Bum
Sun Bum
Sun Bum
Sun Bum
Sun Bum
Sun Bum
Coppertone
Pillowtalk
Pillowtalk
Krusteaz
Krusteaz
Krusteaz
Bearbottom
Knott's Berry Farm
Knott's Berry Farm
Knott's Berry Farm
Knott's Berry Farm
Gap
Gap
Gap
Gap
Gap
Revlon
Revlon
Revlon
Revlon
Walgreens
Walgreens
Walgreens
Walgreens
Marie Claire
Bose
Bose
Bose
Bose
Bose
Heyday
Anker
Anker
Anker
Anker
Belkin
Belkin
Belkin
Belkin
Zumiez
Zumiez
Zumiez
Zumiez
Forever 21
Forever 21
Forever 21
Forever 21
Skullcandy
Skullcandy
Skullcandy
Skullcandy
SONY
SONY
SONY
SONY
HiFiMan
Onzie
Onzie
Onzie
Manduka
Manduka
Manduka
Black Diamond Equipment
Black Diamond Equipment
Black Diamond Equipment
Black Diamond Equipment
Petzl
Petzl
Petzl
Petzl
Urban Outfitters
Urban Outfitters
Urban Outfitters
Urban Outfitters
Hot Topic
Hot Topic
Hot Topic
Hot Topic
Free People
Free People
Free People
Free People
Fashion Nova
Fashion Nova
Fashion Nova
Fashion Nova
Rogue Fitness
Rogue Fitness
Rogue Fitness
Rogue Fitness
Gold's Gym
Gold's Gym
Gold's Gym
Gold's Gym
Apeman Strong
Barbell Apparel
Jade Yoga
John Deere
John Deere
John Deere
John Deere
John Deere
Milwaukee
Milwaukee
Milwaukee
Milwaukee
Dewalt
Men's Wearhouse
Men's Wearhouse
LA Fitness
LA Fitness
LA Fitness
LA Fitness
Welch's
Welch's
Welch's
Welch's
National Geographic
National Geographic
National Geographic
National Geographic
Anheuser-Busch
Anheuser-Busch
Anheuser-Busch
Anheuser-Busch
Venmo
Venmo
Venmo
Venmo
Venmo
Coors Light
Coors Light
Coors Light
Coors Light
KIND Snacks
KIND Snacks
KIND Snacks
KIND Snacks
Bylt Basics
Bylt Basics
Bylt Basics
Asics
Asics
Asics
Asics
Bissell
Bissell
Bissell
Bissell
Cashapp
Cashapp
Cashapp
Cashapp
PayPal
PayPal
Gainful Health
Michelin
Michelin
Hims
Alpha Lion
Roku
Cook unity
Pretty Litter
Byte Tag
Arm & Hammer
Odoban
GoTags
Pup Culture
Dr Squatch
Rockey Money
iheartcats.com
Aura
Endel
Opera
Native
Native
Henson Shaving
Capital One Shopping
Bluehost
Zulily
Zulily
Zulily
Zorka Agency
Walmart
Walmart
Walmart
Walmart
Viralpitch
Viralpitch
Viralpitch
Tinuiti
Tinuiti
Tinuiti
LA Weekly
JPMorgan & Chase
JPMorgan & Chase
JPMorgan & Chase
Starpower Companies
Starpower Companies
Starpower Companies
Waves Audio
Waves Audio
Squatwolf
Squatwolf
Plarium
Plarium
Shein Group
Shein Group
Macy's
Macy's
Macy's
Edible Arrangements
ZURU
ZURU
ZURU
air up
1more
1more
BenQ
BenQ
BenQ
Filabot
Filabot
FlexiSpot
FlexiSpot
FlexiSpot
FlexiSpot
Herman Miller
Herman Miller
Herman Miller
KeySmart
KeySmart
Logitech
Logitech
PVCase
RealVNC Rasperry Pi
RealVNC Rasperry Pi
Brilliant
Iolo System Mechanic
Iolo System Mechanic
Henson Shaving
Mine
Mint Mobile
Mint Mobile
Woo Audio
Vessi Footwear
TUDIA Products
TUDIA Products
Tello
Spikeball
Spikeball
Niu Technologies
Shift Robotics
NexiGo
NexiGo
Satechi
Satechi
Satechi
QCY Makes
QCY Makes
Samsung
Samsung
Samsung
Samsung
Taskrabbit
Taskrabbit
Taskrabbit
Hydrow
Hydrow
Hydrow
Spinn
Blizzard Entertainment
Blizzard Entertainment
Blizzard Entertainment
Blizzard Entertainment
IBM
IBM
IBM
Shopee
Shopee
Shopee
Shopee
Shopee
MVMT
MVMT
MVMT
MVMT
The Home Depot
The Home Depot
The Home Depot
The Home Depot
Activision Blizzard
Activision Blizzard
Activision Blizzard
Activision Publishing
Activision Publishing
Activision Publishing
Activision Publishing
Who What Wear
Tilly's
Tilly's
Tilly's
Misfits Market
Misfits Market
Misfits Market
Kohls
Kohls
Kohls
dbrand
Nintendo of America
Warner Bros. Discovery
Warner Bros. Discovery
XBox Game Studios
Qualcomm
Qualcomm
Verizon
LastPass
Guardio
Rocket Money
Seed
Seed
Cozy Earth
Cozy Earth
Beam Organics
Copilot
Raycon
Raycon
Raycon
Guard.io
Guard.io
Guard.io
Cablemod
AMD
AMD
AMD
Nord Security
Drink LMNT
Drink LMNT
MSI
MSI
MSI
Moosend
Seasonic
MotionGrey
UGREEN
UGREEN
UGREEN
Jukebox Print
Jukebox Print
Dassault Systems
Dassault Systems
Dassault Systems
Dassault Systems
Keeper
Keeper
Keeper
Keeper
SuperMicro
SuperMicro
SuperMicro
Pulseway
Pulseway
Creative Electron
Creative Electron
Acronis
Acronis
Acronis
Acronis
Displate
The Farmers Dog
The Farmers Dog
Uncommon Goods
Bombas
Bombas
Lume Deodorant
Lume Deodorant
Hungry Root
ZocDoc
ZocDoc
Harry's
Harry's
Marine Layer
Marine Layer
Stamps.com
Stamps.com
Earth Breeze
The Beast
Chime
Chime
8 Sleep
8 Sleep
8 Sleep
8 Sleep
Google Meet
Google Meet
Google Meet
Duolingo
Duolingo
Duolingo
Shop
thextremexperience
"""

search_term = "Duo"
lines = contacts.split("\n")
box = 0
for line in lines: 
    line = line.lower()
    box += 1
    if search_term.lower() in line:
        print(True)
        print(line) 
        print(box)
        print()