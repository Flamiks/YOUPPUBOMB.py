numb[10:12]
			numb_5 = numb_1[:4] + ' (' + numb_1[4:6] + ") " + numb_1[6:9] +numb_1[9:11] +numb_1[11:13]
	if country == "by":
		return numb_1, numb_2, numb_3, numb_4, numb_5
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4, numb_5, numb_6, numb_7, numb_8, numb_9, numb_10

def clear():
	if platform == "linux" or platform == "linux2":
		os.system("clear")
	elif platform == "win32":
		os.system("cls")
	else:
		print(colored("\nИзвините наша программа не поддерживает вашу операционную систему ;(\n", "red"))
		exit()

def anim_text(text, speed, color="green"):
	for i in text:
		print(colored(i, color), end="", flush=True)
		time.sleep(speed)

def banner():
	a = open("tools/version.txt", "r")
	ver = a.read().split("\n")[0]
	a.close()

	ru_s = str(len(send.services_list))
	by_s = str(len(send.services_list_by))

	banner = colored("""

	 ▒█████   ██▀███   ██▓ ▒█████   ███▄    █ 
	▒██▒  ██▒▓██ ▒ ██▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
	▒██░  ██▒▓██ ░▄█ ▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
	▒██   ██░▒██▀▀█▄  ░██░▒██   ██░▓██▒  ▐▌██▒
	░ ████▓▒░░██▓ ▒██▒░██░░ ████▓▒░▒██░   ▓██░
	░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
	  ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
	░ ░ ░ ▒    ░░   ░  ▒ ░░ ░ ░ ▒     ░   ░ ░ 
	    ░ ░     ░      ░      ░ ░           ░ """, "red")
парсинге либо имеют свой API.", "green"))
	print("")
	print("")
	print(colored("Советуем вам использовать ваши собственные покупные прокси если хотите сократить блокировку вашего IP у сервисов и иметь хорошую скорость спама", "green"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def inst_logs():
	# Checking File System Access
	try:
		if platform == "linux" or platform == "linux2":
			shutil.copyfile('tools/logs.txt', '/storage/emulated/0/Download/logs.txt')
			shutil.copyfile('tools/error_logs.txt', '/storage/emulated/0/Download/error_logs.txt')
			print(colored("Файлы", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("были сохранены в папку Download на вашем устройстве", "green"))
			print(colored("Пожалуйста отправьте поочередно эти 2 файла нашему боту в телеграм", "green"), colored("https://t.me/orion_feedback_bot", "cyan"))
			print("")
			print("\nНажмите Enter чтобы вернуться назад")
			input()
		elif platform == "win32":
			print("")
			print(colored("Пожалуйста отправьте нашему боту в телеграм", "green"), colored("https://t.me/orion_feedback_bot", "cyan"), colored("поочередно файлы", "green"), colored("logs.txt error_logs.txt", "cyan"), colored("из папки", "green"), colored("tools", "cyan"))
			print("")
			print("\nНажмите Enter чтобы вернуться назад")
			input()
	except:
		print("")
		print(colored("Мы не смогли переместить файлы в нужную директорию", "yellow"))
		print(colored("Возможно у вас для Термукса в настройках разрешения приложению не доступны Файлы и медиаконтент", "yellow"))
		print(colored("Пожалуйста разрешите Термуксу в настройках все нужные разрешения и повторите попытку"))
		print(colored("За помощью по данному вопросу пишите в нашего бота в телеграм"), colored("https://t.me/orion_feedback_bot", "cyan"))
"port": new_pr.split(":")[1],
								  "login": new_pr.split(":")[2],
								  "password": new_pr.split(":")[3],
								  "format": result}
							print(colored("Прокси работает!", "green"))
							time.sleep(2)
							break

				else:
					break
			elif who_pr == "99":
				return 0, 0, 0

	return country_code[ct]+numb, country_code_2[ct], pr

def ICC():
	try:
		anim_text("Проверка интернет соединения...", speed=0.030, color="green")
						if sender_class.checktimeout(serv) == True:
					if proxy_ != None:
						result = sender_class.spam(serv, number, proxy=proxy_["format"])
						if result[1] == "keyboard":
							raise KeyboardInterrupt

						if result[0] == False:
							logs.save_logs(serv, result[0], error=str(result[1]))
						else:
							logs.save_logs(serv, result[0])
						if result[0] == False:
							# Checking the proxy before the next spam attempt
							print(colored("Проверка прокси...", "yellow"))
							if "login" in proxy_:
								test_proxy = proxy.SPC(proxy_["ip"], proxy_["port"], login=proxy_["login"], password=proxy_["password"])
								if test_proxy == False:
									print(colored("Ваш прокси больше не работает!", "red"))
									print("")
									print(colored("[1]", "red"), colored("Да", "green"))
									print(colored("[2]", "red"), colored("Нет", "red"))
									while True:
										print("")
										print(colored("Продолжить спам без прокси?", "yellow"))
										print("")
										how = input(colored("~# ", "red"))
										if how == "2":
											starting_spam = False
											return
										elif how == "1":
											proxy_ = None
											break							if serv == "magnit":
								if result[1]["status_code"] == 200:
									FormattingResponse(200, serv)
								elif result[1]["status_code"] == 422:
									FormattingResponse(429, serv)
							else:
								FormattingResponse(result[0], serv)
						else:
							FormattingResponse(666, serv)
		except KeyboardInterrupt:
			starting_spam = False
			print("\n")
			print(colored("Спам был принудительно оставлен\n", "green"))
			print("Нажмите Enter чтобы вернуть назад")
			try:
				input()
			except KeyboardInterrupt:
				return
			return
		except Exception as e:
			starting_spam = False
			print("\n")
			print(colored("Из-за неизвестной ошибки наша программа выдала ошибку при спаме\n", "yellow"))
			logs.error_logs(str(e))
			print(colored("Данная ошибка была сохранена в логи", "green"))
			print(colored("Пожалуйста отправьте нам файл с логами по инструкции в главном меню чтобы мы могли улучшать наш проект с вашей помощью", "green"))
			print("\nНажмите Enter чтобы вернуть назад")
			try:
				input()
			except KeyboardInterrupt:
				return
			return
