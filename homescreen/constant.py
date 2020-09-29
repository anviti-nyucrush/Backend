from enum import Enum 


class Page(Enum):
    pg1 = "advance_filter"
    pg2 = "filters"
    pg3 = "become_elite_member"
    pg4 = "elite registration1"
    pg5 = "elite registration2"
    pg6 = "elite registration3"
    pg7 = "elite registration4"
    pg8 = "elite registration7 & 8 & 9"
    pg9 = "make payment"
    pg10= "profile card"

class Id(Enum):
    id1 = "ph1"
    id2 = "ph2"
    id3 = "ph3"
    id4 = "ph4"
    id5 = "ph5"
    id6 = "ph6"
    id7 = "ph7"
    id8 = "ph8"
    id9 = "ph9"
    id10 = "ph10"
    id11 = "ph11"
    id12 = "ph12"
    id13 = "ph13"
    id14 = "ph14"
    id15 = "ph15"
    id16 = "ph16"
    id17 = "ph17"
    id18 = "ph18"
    

class ResponseStruct(Enum):
    id = "ph"
    type = "type"
    val = "value"
    multival = "multipleValue"
    title = "title"
    desc = "description"
    switch = "switch"
    min_max_range = "range"
    
class Type(Enum):
    ty1 = "heading"
    ty2 = "text"
    ty3 = "textBox"
    ty4 = "button"
    ty5 = "link"
    ty6 = "multi_select"
    ty7 = "dropdown"
    ty8 = "switch_type1"
    ty9 = "slide_bar"
    ty10= "switch_type2"
    ty11= "muliSelect_cards"
    ty12= "Payment Palceholder"
    ty13= "list"
    

class Heading(Enum):
    hd1 = "Advance Filters"
    hd2 = "Filters"
    hd3 = "Become Elite Member"
    hd4 = "Elite Registration"
    hd5 = "Select a plan"
    hd6 = "Nyu Crush"
    hd7 = "Make Payment"


class Text(Enum):
    tx1 = "Check your elite eligibility now or upgrade your account & unlock interesting features that are designed only for you."
    tx2 = "Connect"
    tx3 = "Send instant chat message without a match"
    tx4 = "Elite"
    tx5 = "Feature in the elite category & select elite people"
    tx6 = "Free"
    tx7 = "No upgrade required"
    tx8 = "PAN number"
    tx9 = "We fetch your PAN details for retrieving your CIBIL score"
    tx10= "Credit Card Details"
    tx11= "This will explain why we are asking for user's PAN details"
    tx12= "No payment will be deducted"
    tx13= "congratualations!"
    tx14= "You're our elite member now" 
    tx15= "Oops!"
    tx16= "Don't worry you can still subscribe"
    tx17= "Become an elite member of Nyu Crush and connect with your ideal match."



class TextBox(Enum):
    tb1 = {
        ResponseStruct.title.value : "Crossover" ,      
        ResponseStruct.desc.value : "Those who have crossed your paths"
    }
    tb2 = {
        ResponseStruct.title.value : "" ,               
        ResponseStruct.desc.value : "Enter PAN number"
    }
    tb3 = {
        ResponseStruct.title.value : "" ,               
        ResponseStruct.desc.value : "Credit Card Details"
    }
    tb4 = {
        ResponseStruct.title.value : "" ,               
        ResponseStruct.desc.value : "Expiry Date MM/YY"
    }
    tb5 = {
        ResponseStruct.title.value : "" ,               
        ResponseStruct.desc.value : "Name as on the Card"
    }
    
         

class Dropdown(Enum):
    dd1 = {
        ResponseStruct.title.value : "Height" ,    
        ResponseStruct.desc.value : "Min: 0'0", 
        ResponseStruct.min_max_range.value : ['120' , '200', 'cm']
    }
    dd2 = {
        ResponseStruct.title.value : "" ,  
        ResponseStruct.desc.value : "Max: 0'0", 
        ResponseStruct.min_max_range.value : ['120' , '200', 'cm']
    }
    dd3 = {
        ResponseStruct.title.value : "Marital Status", 
        ResponseStruct.desc.value : "Select",   
        ResponseStruct.multival.value : ['Separated' , 'Married']
    }
    dd4 = {
        ResponseStruct.title.value : "Religion",
        ResponseStruct.desc.value : "Select",   
        ResponseStruct.multival.value : ['' , '']
    }
    dd5 = {
        ResponseStruct.title.value : "Occupation",     
        ResponseStruct.desc.value : "Select",   
        ResponseStruct.multival.value : ['', '' ]
    }
    

class Switch_type1(Enum):
    s1 = {
        ResponseStruct.title.value : "" ,     
        ResponseStruct.switch.value : ['On' , 'off']
    }
    s5 = {
        ResponseStruct.title.value : "Hide Social Media Friends" ,   
        ResponseStruct.switch.value : ['Show' , 'Hide']
    }


class Switch_type2(Enum):
    s2 = {
        ResponseStruct.title.value : "Drink?",
        ResponseStruct.switch.value : ['Yes' , 'No'], 
        ResponseStruct.desc.value : "Does it matter if the other person drinks?"
    }
    s3 = {
        ResponseStruct.title.value : "Smoke?",
        ResponseStruct.switch.value : ['Yes' , 'No'], 
        ResponseStruct.desc.value : "Does it matter if the other person smokes?"
    }
    s4 = {
        ResponseStruct.title.value : "Like Pets?",
        ResponseStruct.switch.value : ['Yes' , 'No'], 
        ResponseStruct.desc.value : "Does it matter if the other person pets?"
    }
    

class SlideBar(Enum):
    sb1 = {
        ResponseStruct.title.value : "Age" , 
        ResponseStruct.min_max_range.value : ['22' , '32' , 'Yrs']
    }    
    sb2 = {
        ResponseStruct.title.value : "Distance" , 
        ResponseStruct.min_max_range.value : ['Nearby' , '3' , 'Kms']
    }    
    

class MultiSelect(Enum):
    ms1 = {
        ResponseStruct.title.value : "I'm interested in " ,
        ResponseStruct.multival.value : ['Men', 'Women', 'More'] 
    }
    ms2 = {
        ResponseStruct.title.value : "Political View" ,  
        ResponseStruct.multival.value : ['Apolitical', 'Moderate', 'Liberal' , 'Conservative'] 
    }
    ms3 = {
        ResponseStruct.title.value : "Body Type" , 
        ResponseStruct.multival.value : ['Athletic', 'Slim', 'Moderate'] 
    }
    
class Button(Enum):
    bt1 = "Next"
    bt2 = "Save changes"
    bt3 = "Save"
    bt4 = "Subscribe"
    bt5 = "Check Eligibility"
    bt6 = "Continue"
    bt7 = "Submit"
    bt8 = "Start Searching"


class Link(Enum):
    l1 = "SKIP"
    l2 = "Take photo"
    l3 = "Select from Gallery"
    l4 = "Select from Instagram"
    l5 = "Select from Facebook"
    l6 = "Set advance features"    
    l7 = "I don't wish to share details. I'll subscribe instead"

#for membership type descrition
class MultiSelect_card():
    cards =[ 
        {"Duration": "3 Months", "Price" : "Rs. 1000 per month", "Discount" :"" },
        {"Duration": "6 Months", "Price" : "Rs. 1000 per month", "Discount" :"Save 12%" },
        {"Duration": "1 Year",   "Price" : "Rs. 1000 per month", "Discount" :"Save 32%" }   
    ]

#for make_payment screen
class pay(Enum):
    name = "Name"
    pay_type = "Payment Type"
    cg = "Category"
    mode = "mode"

class payment_comp():
    pc1 = {
            pay.mode.value : "Last Used",
            pay.cg.value:[
            {
                pay.name.value : "HDFC Bank",
                pay.pay_type.value : "NetBanking"
            }
            ]
        }
    pc2 ={
            pay.mode.value : "Wallets",
            pay.cg.value:[
            {
                pay.name.value : "Paytm",
                pay.pay_type.value : ""
            },
            {
                pay.name.value : "PhonePay",
                pay.pay_type.value : ""
            } 
            ]
        }
    pc3 = {
            pay.mode.value : "Online Payment",
            pay.cg.value:[
            {
                pay.name.value : "HDFC Bank",
                pay.pay_type.value : "NetBanking"
            },
            {
                pay.name.value : "ICIC Bank",
                pay.pay_type.value : "NetBanking"
            },
            {
                pay.name.value : "Credit, Debit & ATM cards",
                pay.pay_type.value : ""
            },
            {
                pay.name.value : "NetBanking",
                pay.pay_type.value : ""
            } 
            ]
        }
    pc4 = {
            pay.mode.value : "UPI",
            pay.cg.value:[
            {
                pay.name.value : "Google Pay",
                pay.pay_type.value : ""
            },
            {
                pay.name.value : "Pay via UPI",
                pay.pay_type.value : ""
            } 
            ]
        }
       
#User Home Screen
class home():
    
    filters ={ "filter_options" : ['Elite', 'Friend', 'Fling'] }
    otehr_filter = { "other filters" : "<url here>" }
    user_card = {
        "pic_url" : "",
        "name" : "Nataile",
        "age" : "26",
        "bio": "Get busy living or get busy dying",
        "percent_match": "",
        "attributes": ["Fun loving", "Outgoing",""],
    }

