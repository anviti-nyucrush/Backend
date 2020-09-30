from enum import Enum 


class Page(Enum):
    pg1 = "profile with eligibilty strip incomplete - type1"
    pg2 = "profile with eligibilty strip incomplete - type2"
    pg3 = "profile with eligibilty strip complete"
    pg4 = "settings"
    
    

class ResponseStruct(Enum):
    id = "ph"
    type = "type"
    val = "value"
    multival = "multipleValue"
    title = "title"
    desc = "description"
    switch = "switch"
    min_max_range = "range"
    link  = "rediect path"
    

class Type(Enum):
    ty1 = "heading"
    ty2 = "text"
    ty3 = "textBox"
    ty4 = "button"
    ty5 = "link"
    ty6 = "multi_select"
    ty7 = "dropdown"
    ty8 = "switch"
    ty9 = "multival"
    ty10 = "text+link"


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
    id10 = "id10"
    id11 = "ph11"
    id12 = "ph12"
    id13 = "ph13"
    id14 = "ph14"
    id15 = "ph15"
    id16 = "ph16"

class Heading(Enum):
    hd1 = "Complete Profile"
    hd2 = "Settings"

class Text(Enum):
    tx1 = "Your prfile status"
    tx2 = "Complete your profile for maximum flavour."
    tx3 = "Your story"
    tx4 = "Made in India"
    tx5 = "Check your eligibilty"
    tx6 = "Check your eligibily for better match"
    tx7 = "See how others check you out"
    tx8 = "Join the Elite club"


class Switch(Enum):
    s1 = {
        ResponseStruct.title.value : "Show read receipt",
        ResponseStruct.switch.value : ['On' , 'Off']
    }
    s2 = {
        ResponseStruct.title.value : "Show recently active status",
        ResponseStruct.switch.value : ['Show' , 'Hide']
    }
    s3 = {
        ResponseStruct.title.value : "Show distances in" , 
        ResponseStruct.switch.value : ['Km' , 'Mi']
    }
  

class Button(Enum):
    bt1 = "Manage photos"
    bt2 = "Check now"
    
class Link(Enum):
    l1 = "Complete now"
    l2 = "Preview"
    l3 = "Check Now"
    l4 = "View"
    
class TextLink(Enum):
    tl1 = {
        ResponseStruct.title.value : "Notifications settings",
        ResponseStruct.link.value : "<link_path>"
    }
    tl2 = {
        ResponseStruct.title.value : "Help & support",
        ResponseStruct.link.value : "<link_path>"
    }
    tl3 = {
        ResponseStruct.title.value : "Privacy",
        ResponseStruct.link.value : "<link_path>"
    }
    tl4 = {
        ResponseStruct.title.value : "Logout",
        ResponseStruct.link.value : "<link_path>"
    }
    
#class for profile
class profile():
    user_name = "Nataile J. Prince"
    user_photo_link = ""
    user_dob = "24 July 1990"
    profile_status_percent = "58"


