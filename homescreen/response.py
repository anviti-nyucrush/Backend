from .constant import (
    Page, ResponseStruct, Type, Id, Heading, 
    Text, TextBox, MultiSelect, Button, 
    Switch_type1, Switch_type2, Link, 
    Dropdown, SlideBar, MultiSelect_card, 
    payment_comp, home
)

def response_advance_filter(s):
    if(s == Page.pg1.value): 
        return [ 
            { ResponseStruct.id.value : Id.id1.value, ResponseStruct.val.value : Heading.hd1.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value, ResponseStruct.val.value : Switch_type1.s1.value, ResponseStruct.type.value : Type.ty8.value} ,
            { ResponseStruct.id.value : Id.id3.value, ResponseStruct.val.value : MultiSelect.ms1.value, ResponseStruct.type.value : Type.ty6.value} , 
            { ResponseStruct.id.value : Id.id4.value, ResponseStruct.val.value : SlideBar.sb1.value,    ResponseStruct.type.value : Type.ty9.value} , 
            { ResponseStruct.id.value : Id.id5.value, ResponseStruct.val.value : SlideBar.sb2.value,    ResponseStruct.type.value : Type.ty9.value} ,
            { ResponseStruct.id.value : Id.id6.value, ResponseStruct.val.value : TextBox.tb1.value,     ResponseStruct.type.value : Type.ty3.value} , 
            { ResponseStruct.id.value : Id.id7.value, ResponseStruct.val.value : Dropdown.dd1.value,    ResponseStruct.type.value : Type.ty7.value} ,
            { ResponseStruct.id.value : Id.id8.value, ResponseStruct.val.value : Dropdown.dd2.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id9.value, ResponseStruct.val.value : MultiSelect.ms2.value, ResponseStruct.type.value : Type.ty6.value} ,
            { ResponseStruct.id.value : Id.id10.value,ResponseStruct.val.value : MultiSelect.ms3.value, ResponseStruct.type.value : Type.ty6.value} , 
            { ResponseStruct.id.value : Id.id11.value,ResponseStruct.val.value : Dropdown.dd3.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id12.value,ResponseStruct.val.value : Dropdown.dd4.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id13.value,ResponseStruct.val.value : Dropdown.dd5.value,    ResponseStruct.type.value : Type.ty7.value} , 
            { ResponseStruct.id.value : Id.id14.value,ResponseStruct.val.value : Switch_type2.s2.value, ResponseStruct.type.value : Type.ty10.value} , 
            { ResponseStruct.id.value : Id.id15.value,ResponseStruct.val.value : Switch_type2.s3.value, ResponseStruct.type.value : Type.ty10.value} , 
            { ResponseStruct.id.value : Id.id16.value,ResponseStruct.val.value : Switch_type2.s4.value, ResponseStruct.type.value : Type.ty10.value} , 
            { ResponseStruct.id.value : Id.id17.value,ResponseStruct.val.value : Switch_type2.s4.value, ResponseStruct.type.value : Type.ty10.value} , 
            { ResponseStruct.id.value : Id.id18.value,ResponseStruct.val.value : Switch_type1.s5.value, ResponseStruct.type.value : Type.ty8.value}  
        ]

def response_filter(s):
    if(s == Page.pg2.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd2.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : MultiSelect.ms1.value, ResponseStruct.type.value : Type.ty6.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : SlideBar.sb1.value,    ResponseStruct.type.value : Type.ty9.value} , 
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : SlideBar.sb2.value,    ResponseStruct.type.value : Type.ty9.value} , 
            { ResponseStruct.id.value : Id.id5.value,   ResponseStruct.val.value : Switch_type1.s5.value, ResponseStruct.type.value : Type.ty8.value} ,
            { ResponseStruct.id.value : Id.id6.value,   ResponseStruct.val.value : Link.l6.value,         ResponseStruct.type.value : Type.ty5.value}  
         
        ]


def response_subscribe_elite(s):
    if(s == Page.pg3.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd3.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : Text.tx1.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : Text.tx2.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : Text.tx3.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id5.value,   ResponseStruct.val.value : Text.tx4.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id6.value,   ResponseStruct.val.value : Text.tx5.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id7.value,   ResponseStruct.val.value : Text.tx6.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id8.value,   ResponseStruct.val.value : Text.tx7.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id9.value,   ResponseStruct.val.value : Button.bt4.value,      ResponseStruct.type.value : Type.ty4.value} ,            
            { ResponseStruct.id.value : Id.id10.value,  ResponseStruct.val.value : Button.bt5.value,      ResponseStruct.type.value : Type.ty4.value}             
        ]

def response_elite_register1(s):
    if(s == Page.pg4.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd4.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : Text.tx8.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : Text.tx9.value,        ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : TextBox.tb2.value,     ResponseStruct.type.value : Type.ty3.value} ,
            { ResponseStruct.id.value : Id.id5.value,   ResponseStruct.val.value : Button.bt6.value,      ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id6.value,   ResponseStruct.val.value : Link.l7.value,         ResponseStruct.type.value : Type.ty5.value}      
        
        ]


def response_elite_register2(s):
    if(s == Page.pg5.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd4.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : Text.tx10.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : Text.tx11.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : TextBox.tb3.value,     ResponseStruct.type.value : Type.ty3.value} ,
            { ResponseStruct.id.value : Id.id5.value,   ResponseStruct.val.value : TextBox.tb4.value,     ResponseStruct.type.value : Type.ty3.value} ,
            { ResponseStruct.id.value : Id.id6.value,   ResponseStruct.val.value : TextBox.tb5.value,     ResponseStruct.type.value : Type.ty3.value} ,       
            { ResponseStruct.id.value : Id.id7.value,   ResponseStruct.val.value : Button.bt6.value,      ResponseStruct.type.value : Type.ty4.value} ,
            { ResponseStruct.id.value : Id.id8.value,   ResponseStruct.val.value : Text.tx12.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id9.value,   ResponseStruct.val.value : Link.l7.value,         ResponseStruct.type.value : Type.ty5.value}      
            
        ]

def response_elite_register3(s):
    if(s == Page.pg6.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd4.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : Text.tx13.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : Text.tx14.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : Button.bt8.value,      ResponseStruct.type.value : Type.ty4.value} 
        ]

def response_elite_register4(s):
    if(s == Page.pg7.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd4.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : Text.tx15.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : Text.tx16.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : Button.bt4.value,      ResponseStruct.type.value : Type.ty4.value} 
        ]
def response_elite_register5(s):
    if(s == Page.pg8.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd5.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : Heading.hd6.value,     ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : Text.tx17.value,       ResponseStruct.type.value : Type.ty2.value} ,
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : MultiSelect_card.cards,ResponseStruct.type.value : Type.ty11.value} 
        ]

def response_elite_payment(s):
    if(s == Page.pg9.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : Heading.hd7.value,      ResponseStruct.type.value : Type.ty1.value} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : payment_comp.pc1,      ResponseStruct.type.value : Type.ty12.value} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : payment_comp.pc2,      ResponseStruct.type.value : Type.ty12.value} ,
            { ResponseStruct.id.value : Id.id4.value,   ResponseStruct.val.value : payment_comp.pc3,      ResponseStruct.type.value : Type.ty12.value} ,
            { ResponseStruct.id.value : Id.id5.value,   ResponseStruct.val.value : payment_comp.pc4,      ResponseStruct.type.value : Type.ty12.value} ,
            
        ]
def response_profile_card(s):
    if(s == Page.pg10.value):
        return [
            { ResponseStruct.id.value : Id.id1.value,   ResponseStruct.val.value : home.filters,      ResponseStruct.type.value : ''} ,
            { ResponseStruct.id.value : Id.id2.value,   ResponseStruct.val.value : home.otehr_filter, ResponseStruct.type.value : ''} ,
            { ResponseStruct.id.value : Id.id3.value,   ResponseStruct.val.value : home.user_card,    ResponseStruct.type.value : ''} ,
            
            
        ]