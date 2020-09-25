import re
print("dir(re): ", dir(re))

matched_var = re.compile(r'\d\d-\d\d\d-\d\d\d')
str_var = "11-111-111 is my number"

holder = matched_var.search(str_var)
print("Searched Pattern: ", holder.group())

emails = "law@email.com is the orig and not the lawrence@yopmail.com also not this one 24.353"
emails_holder = re.findall(r'[\w.-]+@[\w\.-]+', emails)
print ("emails_holder: ", emails_holder)

using_pipe_sample = re.compile(r'Hello|World')
sample_str = "World Darling my Hello"
match_1 = using_pipe_sample.search(sample_str)
print("match 1: ", match_1.group())

paren_qmark = re.compile(r'(law)?rence')
str = "my name is rence and nick is lawrence not lawrenz or rennz"

res = paren_qmark.search(str)
print("RES: ", res.group())

find_vowels = re.compile(r'[aeiouAEIOU]')
my_str = "Ako ay pinoy. Sa puso't diwa"

all_vowels = find_vowels.findall(my_str)
print("All vowels: ", all_vowels)
print("Len: ", len(all_vowels))

string_to_replace = 'this is the\
    samplestring41thatweneed\
    sogood 111'
pattern = '\s+'
replace = ''
res_101 = re.sub(pattern, replace, string_to_replace)
print("res101: ", res_101)
res_subn = re.subn(pattern, replace, string_to_replace)
print("res subn: ", res_subn)