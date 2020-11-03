guests = ['kyle', 'ashley', 'matt', 'cindy']
print(guests)

print("Please come to dinner at my place tonight " + guests[0].title() + "!")
print("Please come to dinner at my place tonight " + guests[1].title() + "!")
print("Please come to dinner at my place tonight " + guests[2].title() + "!")
print("Please come to dinner at my place tonight " + guests[3].title() + "!")



print(guests[2].title() + " cannot make the party tonight.")
guest_unavailable = 'matt'
guests.remove(guest_unavailable)
print(guests)

guests.insert(2, 'stephen')
print(guests)

print("Please come to dinner at my place tonight " + guests[0].title() + "!")
print("Please come to dinner at my place tonight " + guests[1].title() + "!")
print("Please come to dinner at my place tonight " + guests[2].title() + "!")
print("Please come to dinner at my place tonight " + guests[3].title() + "!")

print("There will be three more guests at the party " + guests[0].title() + "!")
print("There will be three more guests at the party " + guests[1].title() + "!")
print("There will be three more guests at the party " + guests[2].title() + "!")
print("There will be three more guests at the party " + guests[3].title() + "!")

guests.insert(0, 'andie')
print(guests)
guests.insert(2, 'angela')
print(guests)
guests.append('nathan')
print(guests)

print("Please come to dinner at my place tonight " + guests[0].title() + "!")
print("Please come to dinner at my place tonight " + guests[1].title() + "!")
print("Please come to dinner at my place tonight " + guests[2].title() + "!")
print("Please come to dinner at my place tonight " + guests[3].title() + "!")
print("Please come to dinner at my place tonight " + guests[4].title() + "!")
print("Please come to dinner at my place tonight " + guests[5].title() + "!")
print("Please come to dinner at my place tonight " + guests[6].title() + "!")

print("I can only invite two people.")
uninvite1 = guests.pop()
print(guests)
print("Sorry party cancelled!" + " We'll get together next time " + uninvite1.title() + ".")
uninvite2 = guests.pop()
print(guests)
print("Sorry party cancelled!" + " We'll get together next time " + uninvite2.title() + ".")
uninvite3 = guests.pop()
print(guests)
print("Sorry party cancelled!" + " We'll get together next time " + uninvite3.title() + ".")
uninvite4 = guests.pop()
print(guests)
print("Sorry party cancelled!" + " We'll get together next time " + uninvite4.title() + ".")
uninvite5 = guests.pop()
print(guests)
print("Sorry party cancelled!" + " We'll get together next time " + uninvite5.title() + ".")

print(guests)
print("Party's still on! See you tonight " + guests[0].title() + ".")
print("Party's still on! See you tonight " + guests[1].title() + ".")

del guests[0]
del guests[0]
print(guests)









