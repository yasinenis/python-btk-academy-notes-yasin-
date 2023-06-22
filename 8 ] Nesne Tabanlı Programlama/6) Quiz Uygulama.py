# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):      
        return self.answer == answer  
            # herhangi bir question objesindeki (self.answer)answer değeri ile
            # kullanıcının gireceği answer değeri eşit mi 


# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions # ikincisi dışarıdan aldığımız questions olacak
        self.score = 0
        self.questionIndex = 0 # kaçıncı sorudan başlayacak/devam edecek
            # (bu aşamada index numarasını rastgele de yapabilirsin ;))

    def getQuestion(self):      # soruyu indexine falan göre sormayı devamlı kullanamk yerine metod olarak tanımladık devamlı böyle kullanmak daha iyi olur.
        return self.questions[self.questionIndex]
    
    # quiz üzerinden bir soru alınca bunu ekrana yazacak bir metod
    def displayQuestion(self):  
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}') 

        # cevapları sorunun altına yazdırdık
        for q in question.choices:
            print('-' + q)

        # kullanıcı cevap verecek
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f'score: ', self.score)

    def displayProgress(self): # mesela on soruda bir ilerlememizi söylesin
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1 # kaçıncı soruda olduğumuzu söylesin

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100, '*'))

q1 = Question('en iyi programlama dili hangisidir ?',['C#','python','javascript','java'], 'python')
q2 = Question('en popüler programlama dili hangisidir ?',['C#','python','javascript','java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?',['C#','python','javascript','java'], 'python')
questions = [q1, q2, q3]

quiz = Quiz(questions) # biz bu objeyi oluşturur oluşturmaz 17 ve 18 dekiler 0 a eşitleniyor
question = quiz.getQuestion()

quiz.loadQuestion()
