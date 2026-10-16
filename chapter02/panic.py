phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)


# Book ver.1
for i in range(4):
    plist.pop()
#    print(f"pop -> {plist}")
plist.pop(0)
# print(f"pop -> {plist}")
plist.remove("'")
# print(f"remove -> {plist}")
plist.extend([plist.pop(), plist.pop()])
# print(f"extend&pop -> {plist}")
plist.insert(2, plist.pop(3))
# print(f"insert -> {plist}")
new_phrase = "".join(plist)

# myself
# for i in phrase:
# 	plist.remove(i)
#
# for i in 'on tap':
#    plist.append(i)

print(plist)
print(new_phrase)
