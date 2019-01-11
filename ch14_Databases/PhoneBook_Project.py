#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:58:17 2019

@author: maria
"""
import sqlite3
conn=sqlite3.connect("phoneBookProject.db")
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS businesses(business_category TEXT , business_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS people(first_name TEXT , last_name TEXT, adress_line_1 TEXT,adress_line_2 TEXT, adress_line_3 TEXT,postcode TEXT, country TEXT,telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS postcodes(postcode TEXT , latitude TEXT, longitude TEXT)")


def data_entry():
    c.execute("INSERT INTO businesses VALUES('restaurant','Jamie' ,'15 Tarves Way','London','SE109JP','07569655766')")
    conn.commit()
    c.close()
    conn.close()
    
    
import time
import datetime
import random
def people_data_entry():
    people_items=[{"first_name":"Moll","last_name":"Menego","address_line_1":"72 Jenifer Trail","address_line_2":"London","address_line_3":"England","postcode":"WC2H","country":"United Kingdom","telephone_number":"644 543 2902"},
{"first_name":"Rance","last_name":"Zavattero","address_line_1":"36177 4th Street","address_line_2":"Marston","address_line_3":"England","postcode":"ST20","country":"United Kingdom","telephone_number":"454 644 4259"},
{"first_name":"Eleen","last_name":"Zywicki","address_line_1":"41631 Dunning Drive","address_line_2":"Sheffield","address_line_3":"England","postcode":"S33","country":"United Kingdom","telephone_number":"942 918 7431"},
{"first_name":"Prent","last_name":"Glazzard","address_line_1":"35406 Fairfield Terrace","address_line_2":"Church End","address_line_3":"England","postcode":"N3","country":"United Kingdom","telephone_number":"444 755 7392"},
{"first_name":"Del","last_name":"Hutchison","address_line_1":"533 Lawn Circle","address_line_2":"Bradford","address_line_3":"England","postcode":"BD7","country":"United Kingdom","telephone_number":"866 501 4144"},
{"first_name":"Dorena","last_name":"Buttel","address_line_1":"640 Morning Plaza","address_line_2":"Walton","address_line_3":"England","postcode":"CV35","country":"United Kingdom","telephone_number":"468 453 2334"},
{"first_name":"Karlan","last_name":"Voysey","address_line_1":"5 Valley Edge Alley","address_line_2":"Edinburgh","address_line_3":"Scotland","postcode":"EH9","country":"United Kingdom","telephone_number":"951 308 9778"},
{"first_name":"Salomi","last_name":"McGurk","address_line_1":"43777 Michigan Crossing","address_line_2":"Bristol","address_line_3":"England","postcode":"BS41","country":"United Kingdom","telephone_number":"761 875 5654"},
{"first_name":"Reinhold","last_name":"Ferrai","address_line_1":"6 Toban Place","address_line_2":"Buckland","address_line_3":"England","postcode":"CT16","country":"United Kingdom","telephone_number":"184 923 2119"},
{"first_name":"Quinlan","last_name":"Tchir","address_line_1":"6662 Merchant Point","address_line_2":"London","address_line_3":"England","postcode":"W1F","country":"United Kingdom","telephone_number":"932 117 8280"},
{"first_name":"Nathaniel","last_name":"Scroggie","address_line_1":"574 Center Plaza","address_line_2":"Newtown","address_line_3":"England","postcode":"RG20","country":"United Kingdom","telephone_number":"731 924 6691"},
{"first_name":"Christel","last_name":"Imorts","address_line_1":"447 South Pass","address_line_2":"Bristol","address_line_3":"England","postcode":"BS41","country":"United Kingdom","telephone_number":"394 110 6832"},
{"first_name":"Glennis","last_name":"Simmonds","address_line_1":"2234 Bashford Place","address_line_2":"Norton","address_line_3":"England","postcode":"S8","country":"United Kingdom","telephone_number":"161 619 8861"},
{"first_name":"Wally","last_name":"Raecroft","address_line_1":"32529 Colorado Lane","address_line_2":"Twyford","address_line_3":"England","postcode":"LE14","country":"United Kingdom","telephone_number":"503 166 6538"},
{"first_name":"Geno","last_name":"Fritschel","address_line_1":"8 Randy Lane","address_line_2":"Hatton","address_line_3":"England","postcode":"CV35","country":"United Kingdom","telephone_number":"105 252 0118"},
{"first_name":"Hyacinthia","last_name":"Caldicott","address_line_1":"644 Transport Crossing","address_line_2":"Newbiggin","address_line_3":"England","postcode":"NE46","country":"United Kingdom","telephone_number":"899 323 5869"},
{"first_name":"Otha","last_name":"Hobben","address_line_1":"6896 Ridge Oak Circle","address_line_2":"Dean","address_line_3":"England","postcode":"OX7","country":"United Kingdom","telephone_number":"602 955 1224"},
{"first_name":"Dulcinea","last_name":"Townshend","address_line_1":"81 Dakota Pass","address_line_2":"Birmingham","address_line_3":"England","postcode":"B40","country":"United Kingdom","telephone_number":"392 340 0157"},
{"first_name":"Bev","last_name":"Grutchfield","address_line_1":"857 Clemons Street","address_line_2":"London","address_line_3":"England","postcode":"WC1B","country":"United Kingdom","telephone_number":"879 576 6186"},
{"first_name":"Lowrance","last_name":"Southgate","address_line_1":"8 Talmadge Pass","address_line_2":"London","address_line_3":"England","postcode":"SW1E","country":"United Kingdom","telephone_number":"111 564 9550"},
{"first_name":"Maurine","last_name":"MacPeice","address_line_1":"703 Lerdahl Place","address_line_2":"Milton","address_line_3":"England","postcode":"NG22","country":"United Kingdom","telephone_number":"205 942 9228"},
{"first_name":"Baillie","last_name":"Vasilchenko","address_line_1":"67658 Comanche Street","address_line_2":"Buckland","address_line_3":"England","postcode":"CT16","country":"United Kingdom","telephone_number":"609 748 5074"},
{"first_name":"Geralda","last_name":"MacGaughey","address_line_1":"28099 Grayhawk Alley","address_line_2":"Brampton","address_line_3":"England","postcode":"NR34","country":"United Kingdom","telephone_number":"852 100 5874"},
{"first_name":"Kristel","last_name":"Houlworth","address_line_1":"937 Brickson Park Lane","address_line_2":"Bristol","address_line_3":"England","postcode":"BS41","country":"United Kingdom","telephone_number":"898 343 3414"},
{"first_name":"Kent","last_name":"Ingleson","address_line_1":"011 Kennedy Plaza","address_line_2":"Norton","address_line_3":"England","postcode":"NN11","country":"United Kingdom","telephone_number":"176 801 7440"},
{"first_name":"Wright","last_name":"Jolly","address_line_1":"726 Arrowood Junction","address_line_2":"Liverpool","address_line_3":"England","postcode":"L33","country":"United Kingdom","telephone_number":"913 285 5440"},
{"first_name":"Mac","last_name":"Gooderham","address_line_1":"26659 Summerview Place","address_line_2":"Buckland","address_line_3":"England","postcode":"CT16","country":"United Kingdom","telephone_number":"544 985 0728"},
{"first_name":"Jaclin","last_name":"Rochford","address_line_1":"7 Gerald Street","address_line_2":"Newtown","address_line_3":"England","postcode":"RG20","country":"United Kingdom","telephone_number":"638 938 9216"},
{"first_name":"Mair","last_name":"Blethin","address_line_1":"13126 3rd Road","address_line_2":"Wootton","address_line_3":"England","postcode":"NN4","country":"United Kingdom","telephone_number":"290 252 3141"},
{"first_name":"Annetta","last_name":"Belleny","address_line_1":"9 Norway Maple Court","address_line_2":"Thorpe","address_line_3":"England","postcode":"BD23","country":"United Kingdom","telephone_number":"467 373 1663"},
{"first_name":"Baxie","last_name":"Anthill","address_line_1":"88 American Junction","address_line_2":"Dean","address_line_3":"England","postcode":"OX7","country":"United Kingdom","telephone_number":"781 945 8523"},
{"first_name":"Tamarah","last_name":"Perrott","address_line_1":"66053 Westerfield Lane","address_line_2":"West End","address_line_3":"England","postcode":"DN36","country":"United Kingdom","telephone_number":"100 123 5998"},
{"first_name":"Ashla","last_name":"Daughtry","address_line_1":"38346 Katie Hill","address_line_2":"Newport","address_line_3":"England","postcode":"NR29","country":"United Kingdom","telephone_number":"591 565 0421"},
{"first_name":"Simone","last_name":"Stoggell","address_line_1":"404 Lakeland Avenue","address_line_2":"Milton","address_line_3":"England","postcode":"NG22","country":"United Kingdom","telephone_number":"322 918 4187"},
{"first_name":"Tootsie","last_name":"Lant","address_line_1":"901 Boyd Alley","address_line_2":"Stapleford","address_line_3":"England","postcode":"LN6","country":"United Kingdom","telephone_number":"384 461 4246"},
{"first_name":"Hardy","last_name":"Timcke","address_line_1":"53737 Pond Parkway","address_line_2":"Langley","address_line_3":"England","postcode":"SG4","country":"United Kingdom","telephone_number":"934 887 7983"},
{"first_name":"Marika","last_name":"Hatliff","address_line_1":"86057 Hagan Circle","address_line_2":"Merton","address_line_3":"England","postcode":"SW19","country":"United Kingdom","telephone_number":"830 150 3668"},
{"first_name":"Isabelita","last_name":"Wyllcocks","address_line_1":"50 Alpine Circle","address_line_2":"Merton","address_line_3":"England","postcode":"SW19","country":"United Kingdom","telephone_number":"253 349 0800"},
{"first_name":"Kristin","last_name":"Swiggs","address_line_1":"8300 Coolidge Park","address_line_2":"Upton","address_line_3":"England","postcode":"DN21","country":"United Kingdom","telephone_number":"418 976 4971"},
{"first_name":"Lyell","last_name":"Lamers","address_line_1":"43787 Thackeray Drive","address_line_2":"London","address_line_3":"England","postcode":"EC3M","country":"United Kingdom","telephone_number":"477 797 8826"},
{"first_name":"Marsh","last_name":"Claire","address_line_1":"7 Sullivan Road","address_line_2":"Dean","address_line_3":"England","postcode":"OX7","country":"United Kingdom","telephone_number":"338 229 9709"},
{"first_name":"Annecorinne","last_name":"Emeney","address_line_1":"2930 Oneill Lane","address_line_2":"London","address_line_3":"England","postcode":"WC2H","country":"United Kingdom","telephone_number":"721 908 3828"},
{"first_name":"John","last_name":"Abadam","address_line_1":"91 Eastwood Street","address_line_2":"Buckland","address_line_3":"England","postcode":"CT16","country":"United Kingdom","telephone_number":"626 204 3486"},
{"first_name":"Denni","last_name":"Mattia","address_line_1":"133 Westport Hill","address_line_2":"Belfast","address_line_3":"Northern Ireland","postcode":"BT2","country":"United Kingdom","telephone_number":"389 178 8306"},
{"first_name":"Johnath","last_name":"Bernardez","address_line_1":"207 Hanson Way","address_line_2":"Swindon","address_line_3":"England","postcode":"SN1","country":"United Kingdom","telephone_number":"202 280 2960"},
{"first_name":"Judy","last_name":"Pinshon","address_line_1":"8668 Dawn Alley","address_line_2":"Buckland","address_line_3":"England","postcode":"CT16","country":"United Kingdom","telephone_number":"373 463 5022"},
{"first_name":"Jourdain","last_name":"Stovold","address_line_1":"30671 Dahle Drive","address_line_2":"Hatton","address_line_3":"England","postcode":"CV35","country":"United Kingdom","telephone_number":"979 453 4143"},
{"first_name":"Giles","last_name":"Evequot","address_line_1":"773 Lawn Crossing","address_line_2":"Aberdeen","address_line_3":"Scotland","postcode":"AB39","country":"United Kingdom","telephone_number":"310 181 3539"},
{"first_name":"Donia","last_name":"O'Cridigan","address_line_1":"3 Northport Court","address_line_2":"Newtown","address_line_3":"England","postcode":"RG20","country":"United Kingdom","telephone_number":"610 816 4900"},
{"first_name":"Kaila","last_name":"Farmloe","address_line_1":"070 Truax Plaza","address_line_2":"Horton","address_line_3":"England","postcode":"BS37","country":"United Kingdom","telephone_number":"996 445 8280"},
{"first_name":"Bret","last_name":"Abade","address_line_1":"44 Mitchell Point","address_line_2":"Buckland","address_line_3":"England","postcode":"CT16","country":"United Kingdom","telephone_number":"657 738 0553"},
{"first_name":"Keven","last_name":"Vokes","address_line_1":"88988 Bluejay Trail","address_line_2":"Church End","address_line_3":"England","postcode":"N3","country":"United Kingdom","telephone_number":"493 272 8932"},
{"first_name":"Elton","last_name":"McGunley","address_line_1":"80059 Northwestern Street","address_line_2":"Edinburgh","address_line_3":"Scotland","postcode":"EH9","country":"United Kingdom","telephone_number":"303 738 7203"},
{"first_name":"Judye","last_name":"Ivashnikov","address_line_1":"2 Hooker Lane","address_line_2":"Manchester","address_line_3":"England","postcode":"M14","country":"United Kingdom","telephone_number":"122 287 5048"},
{"first_name":"Anissa","last_name":"Thys","address_line_1":"18 Park Meadow Junction","address_line_2":"Church End","address_line_3":"England","postcode":"CB4","country":"United Kingdom","telephone_number":"534 203 4940"},
{"first_name":"Sybil","last_name":"Quipp","address_line_1":"3 Loftsgordon Hill","address_line_2":"Hatton","address_line_3":"England","postcode":"CV35","country":"United Kingdom","telephone_number":"699 522 4713"},
{"first_name":"Joycelin","last_name":"Bielfeld","address_line_1":"66 Northwestern Crossing","address_line_2":"Middleton","address_line_3":"England","postcode":"LE16","country":"United Kingdom","telephone_number":"886 129 5678"},
{"first_name":"Phaedra","last_name":"Skein","address_line_1":"63 Lotheville Court","address_line_2":"Marston","address_line_3":"England","postcode":"ST20","country":"United Kingdom","telephone_number":"317 675 0110"},
{"first_name":"Erika","last_name":"Shulem","address_line_1":"7253 Gina Plaza","address_line_2":"Merton","address_line_3":"England","postcode":"SW19","country":"United Kingdom","telephone_number":"894 719 7578"},
{"first_name":"Fields","last_name":"Dimock","address_line_1":"4 Carey Crossing","address_line_2":"Carlton","address_line_3":"England","postcode":"DL8","country":"United Kingdom","telephone_number":"203 473 6811"},
{"first_name":"Ruddie","last_name":"Twelftree","address_line_1":"398 International Lane","address_line_2":"Twyford","address_line_3":"England","postcode":"LE14","country":"United Kingdom","telephone_number":"744 363 8711"},
{"first_name":"Damita","last_name":"Bulluck","address_line_1":"7 Forster Center","address_line_2":"Denton","address_line_3":"England","postcode":"M34","country":"United Kingdom","telephone_number":"920 816 4666"},
{"first_name":"Caron","last_name":"Seedhouse","address_line_1":"8330 Grim Parkway","address_line_2":"London","address_line_3":"England","postcode":"W1F","country":"United Kingdom","telephone_number":"497 215 6966"},
{"first_name":"Monique","last_name":"Popham","address_line_1":"04 Derek Center","address_line_2":"Swindon","address_line_3":"England","postcode":"SN1","country":"United Kingdom","telephone_number":"683 618 2038"},
{"first_name":"Wylie","last_name":"De Angelis","address_line_1":"77 Morning Point","address_line_2":"Swindon","address_line_3":"England","postcode":"SN1","country":"United Kingdom","telephone_number":"939 651 4212"},
{"first_name":"Thorsten","last_name":"Heare","address_line_1":"42178 Hagan Avenue","address_line_2":"East End","address_line_3":"England","postcode":"BH21","country":"United Kingdom","telephone_number":"662 145 9592"},
{"first_name":"Clemmy","last_name":"Coupe","address_line_1":"275 Beilfuss Center","address_line_2":"Horton","address_line_3":"England","postcode":"BS37","country":"United Kingdom","telephone_number":"416 825 8935"},
{"first_name":"Alysa","last_name":"Bondley","address_line_1":"624 Dryden Park","address_line_2":"Walton","address_line_3":"England","postcode":"CV35","country":"United Kingdom","telephone_number":"561 354 8496"},
{"first_name":"Hillary","last_name":"Puckey","address_line_1":"8 Sheridan Lane","address_line_2":"Swindon","address_line_3":"England","postcode":"SN1","country":"United Kingdom","telephone_number":"401 992 7307"},
{"first_name":"Eve","last_name":"McHardy","address_line_1":"81630 Gina Place","address_line_2":"Brampton","address_line_3":"England","postcode":"NR34","country":"United Kingdom","telephone_number":"879 946 5358"},
{"first_name":"Cori","last_name":"Viant","address_line_1":"2256 Cascade Way","address_line_2":"Ford","address_line_3":"England","postcode":"GL54","country":"United Kingdom","telephone_number":"619 382 2030"},
{"first_name":"Cale","last_name":"Lamke","address_line_1":"79763 Oakridge Point","address_line_2":"Newton","address_line_3":"England","postcode":"NG34","country":"United Kingdom","telephone_number":"774 636 5651"},
{"first_name":"Prince","last_name":"Filipyev","address_line_1":"5145 Londonderry Court","address_line_2":"Ford","address_line_3":"England","postcode":"GL54","country":"United Kingdom","telephone_number":"954 536 4562"},
{"first_name":"Harriett","last_name":"Burstowe","address_line_1":"8578 Spohn Avenue","address_line_2":"Weston","address_line_3":"England","postcode":"GU32","country":"United Kingdom","telephone_number":"587 711 2548"},
{"first_name":"Minny","last_name":"Rubenchik","address_line_1":"7318 Northview Pass","address_line_2":"Seaton","address_line_3":"England","postcode":"LE15","country":"United Kingdom","telephone_number":"979 573 9917"},
{"first_name":"Kissee","last_name":"Pancoast","address_line_1":"8 Warner Circle","address_line_2":"Newton","address_line_3":"Scotland","postcode":"IV1","country":"United Kingdom","telephone_number":"827 415 9594"},
{"first_name":"Jennie","last_name":"Olivet","address_line_1":"1287 Grayhawk Hill","address_line_2":"Liverpool","address_line_3":"England","postcode":"L33","country":"United Kingdom","telephone_number":"469 853 4175"},
{"first_name":"Pierette","last_name":"Netting","address_line_1":"10 Lighthouse Bay Place","address_line_2":"London","address_line_3":"England","postcode":"W1F","country":"United Kingdom","telephone_number":"322 991 9083"},
{"first_name":"Joey","last_name":"Pautot","address_line_1":"92 Johnson Pass","address_line_2":"Weston","address_line_3":"England","postcode":"GU32","country":"United Kingdom","telephone_number":"454 671 8173"},
{"first_name":"Sal","last_name":"Hymas","address_line_1":"42279 Everett Road","address_line_2":"Norton","address_line_3":"England","postcode":"S8","country":"United Kingdom","telephone_number":"934 279 3427"},
{"first_name":"Shalom","last_name":"Waudby","address_line_1":"68 Hanson Center","address_line_2":"Newtown","address_line_3":"England","postcode":"RG20","country":"United Kingdom","telephone_number":"995 772 4154"},
{"first_name":"Farrah","last_name":"Hofler","address_line_1":"44163 Northfield Avenue","address_line_2":"Burnside","address_line_3":"Scotland","postcode":"EH52","country":"United Kingdom","telephone_number":"104 405 7368"},
{"first_name":"Dal","last_name":"Algie","address_line_1":"205 Karstens Point","address_line_2":"Sheffield","address_line_3":"England","postcode":"S1","country":"United Kingdom","telephone_number":"885 892 7119"},
{"first_name":"Dido","last_name":"Staines","address_line_1":"33 Dawn Avenue","address_line_2":"Newton","address_line_3":"Scotland","postcode":"IV1","country":"United Kingdom","telephone_number":"725 982 7391"},
{"first_name":"Perren","last_name":"Boater","address_line_1":"6 Karstens Pass","address_line_2":"Upton","address_line_3":"England","postcode":"DN21","country":"United Kingdom","telephone_number":"173 105 2013"},
{"first_name":"Saundra","last_name":"Crutch","address_line_1":"51838 North Hill","address_line_2":"Upton","address_line_3":"England","postcode":"WF9","country":"United Kingdom","telephone_number":"259 246 0508"},
{"first_name":"Archaimbaud","last_name":"Franzman","address_line_1":"1082 Beilfuss Center","address_line_2":"Newton","address_line_3":"England","postcode":"NG34","country":"United Kingdom","telephone_number":"136 575 5441"},
{"first_name":"Wilbert","last_name":"Watsham","address_line_1":"01 Eastlawn Drive","address_line_2":"Upton","address_line_3":"England","postcode":"WF9","country":"United Kingdom","telephone_number":"296 420 4586"},
{"first_name":"Wallis","last_name":"Ferrieri","address_line_1":"8084 Corscot Park","address_line_2":"Dean","address_line_3":"England","postcode":"OX7","country":"United Kingdom","telephone_number":"976 530 5091"},
{"first_name":"Michel","last_name":"Connor","address_line_1":"70511 Ridge Oak Place","address_line_2":"Merton","address_line_3":"England","postcode":"SW19","country":"United Kingdom","telephone_number":"568 541 4411"},
{"first_name":"Romola","last_name":"Thicking","address_line_1":"19671 New Castle Park","address_line_2":"Swindon","address_line_3":"England","postcode":"SN1","country":"United Kingdom","telephone_number":"777 900 5361"},
{"first_name":"Dallas","last_name":"Copas","address_line_1":"5450 Jenifer Point","address_line_2":"Norton","address_line_3":"England","postcode":"S8","country":"United Kingdom","telephone_number":"211 899 8511"},
{"first_name":"Melitta","last_name":"Deakes","address_line_1":"406 Loeprich Street","address_line_2":"Newtown","address_line_3":"England","postcode":"RG20","country":"United Kingdom","telephone_number":"963 685 8508"},
{"first_name":"Catherin","last_name":"Felce","address_line_1":"55437 Mayfield Hill","address_line_2":"Hatton","address_line_3":"England","postcode":"CV35","country":"United Kingdom","telephone_number":"443 414 9812"},
{"first_name":"Bab","last_name":"Dabes","address_line_1":"492 Hoffman Junction","address_line_2":"Horton","address_line_3":"England","postcode":"BS37","country":"United Kingdom","telephone_number":"496 305 4797"},
{"first_name":"Rosco","last_name":"Tassel","address_line_1":"025 Bunting Center","address_line_2":"West End","address_line_3":"England","postcode":"DN36","country":"United Kingdom","telephone_number":"463 117 2684"},
{"first_name":"Ethelda","last_name":"Rapkins","address_line_1":"2082 Reinke Point","address_line_2":"Burnside","address_line_3":"Scotland","postcode":"EH52","country":"United Kingdom","telephone_number":"796 202 0999"},
{"first_name":"Galvin","last_name":"Papez","address_line_1":"46074 Anniversary Point","address_line_2":"Birmingham","address_line_3":"England","postcode":"B40","country":"United Kingdom","telephone_number":"442 577 0414"},
{"first_name":"Seka","last_name":"Hann","address_line_1":"145 Northport Way","address_line_2":"Carlton","address_line_3":"England","postcode":"DL8","country":"United Kingdom","telephone_number":"499 785 4409"},
{"first_name":"Dominga","last_name":"Smylie","address_line_1":"68 Menomonie Parkway","address_line_2":"Manchester","address_line_3":"England","postcode":"M14","country":"United Kingdom","telephone_number":"828 568 2515"}]
   
    for item in people_items:
        #print("first item: ",item)
        #print(type(item))
        #print("-------------------------------")
        key_list=list(item.keys())
        values_list=list(item.values())
        #print(key_list)
        #print(values_list)
        c.execute("INSERT INTO people(first_name,last_name,adress_line_1,adress_line_2,adress_line_3,postcode,country,telephone_number) VALUES(?,?,?,?,?,?,?,?)", (values_list))
        conn.commit()
    
    
    


#create_table()
people_data_entry()