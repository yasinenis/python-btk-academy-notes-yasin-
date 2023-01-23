n_tasks = ['n1','n2','n3','n4','n5']
d_tasks = ['d1','d2']
otherTasks = []
completedTasks = []
devamEdenTasks = []


completed = input('Tamamlanan Görev Giriniz : ')
onGoing = input('Devam Eden Görev Giriniz : ')


completedTasks.append(completed)
devamEdenTasks.append(onGoing)

d_tasks.remove(completed)

print(f'Tamamlanan Görevler : \n{completedTasks}')
print(f'Devam Eden Görevler : \n{devamEdenTasks} ')


