from flitscore.models import * 

# needed for registering to developer.salesforce.com

sfdc_register = {"url":obj(objtype="chrome",input="https://developer.salesforce.com")}
sfdc = {"url":obj(objtype="chrome",input="https://avconglobal-dev-ed.my.salesforce.com/")}

#https://fa-eqng-dev11-saasfademo1.ds-fa.oraclepdemos.com/	Paul.Cook	CHDG&57fa

oca_slow = {
    "url":obj(objtype="chrome",input="https://fa-eqng-dev11-saasfademo1.ds-fa.oraclepdemos.com/"),
    "users":
            {
                "FinanceAdmin":{"username":"Paul.Cook","name":"Paul.Cook","secret":r"CHDG&57fa"}                
            }
}

oca = {
    "url":obj(objtype="chrome",input="https://fa-eseb-saasfademo1.ds-fa.oraclepdemos.com/"),
    "users":
            {
                "FinanceAdmin":{"username":"Dave.Parker","name":"Dave Parker","secret":r"AH2sf1!7$"}
                
            }
}

