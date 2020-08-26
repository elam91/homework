fish_list = ['blowfish', 'clownfish', 'catfish', 'octopus']
fish_list2 = [fish for fish in fish_list if fish != 'octopus']
fish_list3 = ["blowwwww" if fish ==
              "blowfish" else fish for fish in fish_list if fish != 'octopus']
print(fish_list2)
print(fish_list3)
