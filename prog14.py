import os

os.chdir('C:/Users/e-ric/Videos/')

print(os.getcwd())

for f in os.listdir():
	f_name, f_ext = os.path.splitext(f)
	f_title, f_course, f_num = f_name.split('-')

	f_title = f_title.strip()
	f_course = f_couse.strip()
	f_num = f_num.strip()[1:].zfill(2)


	new_name = '{}-{}{}'.format(f_title, f_num)

	os.rename(f, new_name)
