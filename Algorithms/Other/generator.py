"""
Написать генератор, который читает переданный по имени файл по словам

rfbw = read_file_by_words ('file.txt')
print (next (rfbw) ) # Получаем 1 слово print (rfbw. send (5) ) # Получаем 5 слов
for word in rfbw:
    print(word) # Получаем по 1 слову
"""

def num_generator():
    num = 0
    num_cnt = 0
    while num < 11:
        if num_cnt:
            num_stack = []
            for i in range(num_cnt):
                num_stack.append(num)
                num += 1
        else:
            num_stack = [num]
            num += 1
        num_cnt = yield num_stack


ttt = num_generator()
# print(next(ttt))
# print(ttt.send(5))
# print(ttt.send(5))
# print(next(ttt))

# for i in ttt:
#     print(i)
#
# for i in ttt:
#     print(i)

import multiprocessing

def append_to_list(shared_list):
    shared_list.append(1)

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        shared_list = manager.list()
        processes = [multiprocessing.Process(target=append_to_list, args=(shared_list,)) for _ in range(4)]

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        print("Модифицированный список:", shared_list)