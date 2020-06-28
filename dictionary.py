# # empty dictionary
ডিকশনারী = {}
# # আমার_তথ্য = {key:value}
আমার_তথ্য = {"নাম":"জুবেল"," বয়স ":"২৪","ঠিকানা":"ঢাকা","রোল": '১',}

print(আমার_তথ্য)

for চাবি in আমার_তথ্য:
    print(আমার_তথ্য[চাবি])  # # here we print value by key
    
for চাবি in আমার_তথ্য:
    print(চাবি) # # here we print only key
    


# dictionary with integer keys
ফলের_লিস্ট = {1: 'আপেল', 2: "কমলা",3: "লিচু",4: "জাম",}
 
# # get dict value with many system
# print (ফলের_লিস্ট)
# print (ফলের_লিস্ট[1])
# print (ফলের_লিস্ট.get(1))

# # delete 1 dict from last position
ফলের_লিস্ট.popitem()
print(ফলের_লিস্ট)
ফলের_লিস্ট.pop(2) # # dict.pop(key)
print(ফলের_লিস্ট)

# # nested dictionary

সকল_লোকজন =  {
            1: {"নাম":"সুশেন","বয়স":"৩০","ঠিকানা":"ঢাকা"},
            2: {"নাম":"জুবেল","বয়স":"২৪","ঠিকানা":"ঢাকা"},
            }
 
print(সকল_লোকজন[1]['নাম'])
print(সকল_লোকজন[1]['বয়স'])
print(সকল_লোকজন[1]['ঠিকানা'])

# # script code

# from script import get_all_list, get_rank_name_list, get_rank_list

# # #  this dict create by {'rank':rank,"name":"name"} from the script
# coin_market_top_list = get_rank_name_list(10) ## we can provide any number of position list by get_rank_name_list(50). if empty it will provide top 100 list

# for single_rank in coin_market_top_list:
#     print(single_rank)
    

# # #  this dict create by {rank:name}(key:value)  from the script
# rank_list = get_rank_list(20)

# print(rank_list)

# single_dict = rank_list[0]

# print(single_dict['1'])



# some example of tuple . Its use only for fixed element

আমার_৫_প্রিয়_কালার = ('সবুজ','নীল','কমলা','সাদা','বেগুনী')

print(আমার_৫_প্রিয়_কালার)
print(আমার_৫_প্রিয়_কালার[2])

আমার_৫_প্রিয়_কালার[1] = "হলুদ"  
print(আমার_৫_প্রিয়_কালার) ## get error when want to update or remove its a fixed value