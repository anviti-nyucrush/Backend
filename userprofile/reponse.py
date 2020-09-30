from .constant import (
    Page, ResponseStruct, Type, Id, Heading, 
    Text, TextBox, MultiSelect, Button, 
    Switch, Link, Dropdown, 
    profile, TextLink
)

def response_userprofile_incomplete1(s):
    if(s == Page.pg1.value):
        return [
            { 
                ResponseStruct.id.value : Id.id1.value, 
                ResponseStruct.val.value : profile.user_photo_link,    
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id2.value, 
                ResponseStruct.val.value : Button.bt1.value,    
                ResponseStruct.type.value : Type.ty4.value
            },
            { 
                ResponseStruct.id.value : Id.id3.value, 
                ResponseStruct.val.value : profile.user_name,    
                ResponseStruct.type.value : Type.ty2.value
            }, 
            { 
                ResponseStruct.id.value : Id.id4.value,
                ResponseStruct.val.value : profile.user_dob,     
                ResponseStruct.type.value : Type.ty2.value
            }, 
            { 
                ResponseStruct.id.value : Id.id5.value, 
                ResponseStruct.val.value : [ 
                    Text.tx1.value,
                    profile.profile_status_percent    
                ],
                ResponseStruct.type.value : Type.ty9.value
            }, 
            { 
                ResponseStruct.id.value : Id.id6.value, 
                ResponseStruct.val.value : Text.tx2.value, 
                ResponseStruct.type.value : Type.ty2.value
            }, 
            { 
                ResponseStruct.id.value : Id.id7.value, 
                ResponseStruct.val.value : Link.l1.value,     
                ResponseStruct.type.value : Type.ty5.value
            },
            { 
                ResponseStruct.id.value : Id.id8.value, 
                ResponseStruct.val.value : Text.tx3.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id9.value, 
                ResponseStruct.val.value : Text.tx4.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id10.value, 
                ResponseStruct.val.value : Text.tx5.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id11.value, 
                ResponseStruct.val.value : Text.tx6.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id12.value, 
                ResponseStruct.val.value : Button.bt2.value,     
                ResponseStruct.type.value : Type.ty2.value
            }
        ]

def response_userprofile_incomplete2(s):
    if(s == Page.pg2.value):
        return [
            { 
                ResponseStruct.id.value : Id.id1.value, 
                ResponseStruct.val.value : profile.user_photo_link,    
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id2.value, 
                ResponseStruct.val.value : Button.bt1.value,    
                ResponseStruct.type.value : Type.ty4.value
            },
            { 
                ResponseStruct.id.value : Id.id3.value, 
                ResponseStruct.val.value : profile.user_name,    
                ResponseStruct.type.value : Type.ty2.value
            }, 
            { 
                ResponseStruct.id.value : Id.id4.value,
                ResponseStruct.val.value : profile.user_dob,     
                ResponseStruct.type.value : Type.ty2.value
            }, 
            { 
                ResponseStruct.id.value : Id.id5.value, 
                ResponseStruct.val.value : [ 
                    Text.tx1.value,
                    profile.profile_status_percent    
                ],
                ResponseStruct.type.value : Type.ty9.value
            }, 
            { 
                ResponseStruct.id.value : Id.id6.value, 
                ResponseStruct.val.value : Text.tx2.value, 
                ResponseStruct.type.value : Type.ty2.value
            }, 
            { 
                ResponseStruct.id.value : Id.id7.value, 
                ResponseStruct.val.value : Link.l1.value,     
                ResponseStruct.type.value : Type.ty5.value
            },
            { 
                ResponseStruct.id.value : Id.id8.value, 
                ResponseStruct.val.value : Text.tx7.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id9.value, 
                ResponseStruct.val.value : Link.l2.value,     
                ResponseStruct.type.value : Type.ty5.value
            },
            { 
                ResponseStruct.id.value : Id.id10.value, 
                ResponseStruct.val.value : Text.tx8.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id11.value, 
                ResponseStruct.val.value : Link.l3.value,     
                ResponseStruct.type.value : Type.ty5.value
            },
            { 
                ResponseStruct.id.value : Id.id12.value, 
                ResponseStruct.val.value : Text.tx3.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id13.value, 
                ResponseStruct.val.value : Text.tx4.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id14.value, 
                ResponseStruct.val.value : Text.tx5.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id15.value, 
                ResponseStruct.val.value : Text.tx6.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id16.value, 
                ResponseStruct.val.value : Button.bt2.value,     
                ResponseStruct.type.value : Type.ty2.value
            }
        ]

def response_userprofile_complete(s):
    if(s == Page.pg3.value):
        return [
            { 
                ResponseStruct.id.value : Id.id1.value, 
                ResponseStruct.val.value : profile.user_photo_link,    
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id2.value, 
                ResponseStruct.val.value : Button.bt1.value,    
                ResponseStruct.type.value : Type.ty4.value
            },
            { 
                ResponseStruct.id.value : Id.id3.value, 
                ResponseStruct.val.value : profile.user_name,    
                ResponseStruct.type.value : Type.ty2.value
            }, 
            { 
                ResponseStruct.id.value : Id.id4.value,
                ResponseStruct.val.value : profile.user_dob,     
                ResponseStruct.type.value : Type.ty2.value
            }, 
            { 
                ResponseStruct.id.value : Id.id5.value, 
                ResponseStruct.val.value : [ 
                    Text.tx1.value,
                    profile.profile_status_percent    
                ],
                ResponseStruct.type.value : Type.ty9.value
            },
            { 
                ResponseStruct.id.value : Id.id6.value, 
                ResponseStruct.val.value : Link.l4.value,     
                ResponseStruct.type.value : Type.ty5.value
            },  
            { 
                ResponseStruct.id.value : Id.id6.value, 
                ResponseStruct.val.value : Text.tx7.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id9.value, 
                ResponseStruct.val.value : Link.l2.value,     
                ResponseStruct.type.value : Type.ty5.value
            },
            
            { 
                ResponseStruct.id.value : Id.id10.value, 
                ResponseStruct.val.value : Text.tx3.value,     
                ResponseStruct.type.value : Type.ty2.value
            },
            { 
                ResponseStruct.id.value : Id.id13.value, 
                ResponseStruct.val.value : Text.tx4.value,     
                ResponseStruct.type.value : Type.ty2.value
            }
        ]

def response_settings(s):
    if(s == Page.pg4.value):
        return [
            { 
                ResponseStruct.id.value : Id.id1.value, 
                ResponseStruct.val.value : Heading.hd2.value,    
                ResponseStruct.type.value : Type.ty1.value
            },
            { 
                ResponseStruct.id.value : Id.id2.value, 
                ResponseStruct.val.value : Switch.sw1.value,    
                ResponseStruct.type.value : Type.ty8.value
            },
            { 
                ResponseStruct.id.value : Id.id3.value, 
                ResponseStruct.val.value : Switch.sw2.value,    
                ResponseStruct.type.value : Type.ty8.value
            },
            { 
                ResponseStruct.id.value : Id.id4.value, 
                ResponseStruct.val.value : Switch.sw3.value,    
                ResponseStruct.type.value : Type.ty8.value
            },
            { 
                ResponseStruct.id.value : Id.id5.value, 
                ResponseStruct.val.value : TextLink.tl1.value,    
                ResponseStruct.type.value : Type.ty10.value
            },
            { 
                ResponseStruct.id.value : Id.id6.value, 
                ResponseStruct.val.value : TextLink.tl2.value,    
                ResponseStruct.type.value : Type.ty10.value
            },
            { 
                ResponseStruct.id.value : Id.id7.value, 
                ResponseStruct.val.value : TextLink.tl3.value,    
                ResponseStruct.type.value : Type.ty10.value
            },
            { 
                ResponseStruct.id.value : Id.id8.value, 
                ResponseStruct.val.value : TextLink.tl4.value,    
                ResponseStruct.type.value : Type.ty10.value
            }            
        ]
