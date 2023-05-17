# -- coding: utf-8 --

max_ary=0
ent_list = []
rel_list = []
strfacts = []
filename = "test"


with open("./n-ary_{}.json".format(filename), "r") as f:
    lines = f.readlines()
for k in range(len(lines)):
    line = lines[k]
    dic = eval(line)
    if dic['N'] > max_ary:
        max_ary = dic['N']
    tmp_fact = []
    str_list = [x.strip('":') for x in line.strip('\n{}').split()]
    role_list = []
    for tmp_role in str_list:
        if tmp_role[0] == 'P':
            if type(dic[tmp_role]) != list:
                role_list.append(tmp_role)
                tmp_fact.append(dic[tmp_role])
                ent_list.append(dic[tmp_role])
            else:
                for val0 in dic[tmp_role]:
                    role_list.append(tmp_role)
                    tmp_fact.append(val0)
                    ent_list.append(val0)
    sorted_role = sorted(enumerate(role_list), key=lambda x: x[1])
    role_list = [i[1] for i in sorted_role]
    idx = [i[0] for i in sorted_role]
    tmp_fact = [tmp_fact[id] for id in idx]
    tmp_rel = '/'.join(role_list)
    tmp_fact = [tmp_rel] + tmp_fact
    rel_list.append(tmp_rel)
    strfacts.append(tmp_fact)
    
print(max_ary)   
 
#
# with open("./{}.txt".format(filename), "w") as f:
#     for fact in strfacts:
#         for i in range(len(fact)):
#             if i != len(fact)-1:
#                 f.write(fact[i]+"\t")
#             else:
#                 f.write(fact[i])
#         f.write("\n")

# for file in ["train", "valid", "test"]:
    # with open("./{}.txt".format(file), "r") as f:
        # lines = f.readlines()
        # for line in lines:
            # line = line.strip("\n").split("\t")
            # rel = line[0]
            # rel_list.add(rel)
            # ents = line[1:]
            # for ent in ents:
                # ent_list.add(ent)

# with open("./entities.dict", "w") as f:
    # for i, ent in enumerate(ent_list):
        # f.write(str(i)+"\t"+ent+"\n")

# with open("./relations.dict", "w") as f:
    # for i, rel in enumerate(rel_list):
        # f.write(str(i)+"\t"+rel+"\n")




