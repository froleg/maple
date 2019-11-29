
import _thread as thread, time
def counter(myId, count): # эта функция выполняется в потоках
  for i in range(count):
    mutex.acquire()
     # имитировать работу
    print('[%s] => %s' % (myId, i)) # теперь работа функции print
    # не будет прерываться
    mutex.release()
    time.sleep(1)
mutex = thread.allocate_lock() # создать объект блокировки
for i in range(5): # породить 5 потоков выполнения
   thread.start_new_thread(counter, (i, 5)) # каждый поток выполняет 5 циклов
time.sleep(30)
print('Main thread exiting.') # задержать выход из программ