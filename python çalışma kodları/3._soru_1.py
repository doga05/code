
"""
3/3

"""

"""
class LinkedStack:
    class _Node:
        __slots__ = "_element" , "_next"
        def __init__(self,element,next):
            self._element=element
            self._next=next
    def __init__(self):
        self._head = None
        self._size= 0
        self._num_of_calls = 0 
        
"""



def pop(self):          #pop fonksyonu tanımlanmıştır
    if self.is_empty():     #is_empty fonksyonu çağırılıyor eğer bu doğruysa fonksyonun dönüşü iç kısma geçiyor
    
        print("Stack is empty") #"stack is empty" ekrana yazılıyor
        return None #if fonksyonun içine girildiyse None döndürülüyor ve bu fonksyondan çıkılıyor
    
    answer = self._head._element #answer değişkeni yığının tepe elemanındaki yazılan bilgiye eşitleniyor
    self._head=self._head._next #yığında (top) self._head'i tutan değişkenden sonra gelen düğüm, self._head değişkenine atanıyor
    self._size -= 1 #self._size değişkenini 1 azaltıyor
    self._num_of_calls += 1 #self._num_of_calls 1 arttırılıyor
    return answer #answer değişkeninin içeriği dışarıya geri dönüş değeri olarak veriliyor

def print_stack(self): #print_stack() fonksyonu tanımlanıyor fakat parametre almıyor.
    j = self._head #yığının (top) tepe düğümünü gösteren değişken [self._head], j değişkenine atanıyor. Bu j değişkeni iterasyon için kullanılacak
    for i in range(self._size): #for döngüsü kuruluyor, j=0dan self._size - 1'e kadar devam edecektir
        print("stack element", i ,"is", j._element) #ekrana döküyoruz
        j = j._next #j değişkeni j'den sonraki düğüme eşitleniyor *(yığında bir sonraki düğüme geçiliyor)
        self._num_of_calls +=1 #self._num__of_calls 1 arttırılıyor
""" 
4/3       
"""
"""
class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next): 
            self._element = element 
            self._next = next 
    def __init__(self):
        self._head = None
        self._size = 0
        self._default = -99
        self._element_err = 0
        self._top_is_called = 0
"""
def push(self, e): #push fonksyonu atanıyor "e" parametresi alınıyor
     print('assigned element is -> ', e) #parametre ekrana yazılıyor
     if e > 10: #"e" parametresi 10'dan büyükse if fonksyonunun içine giriliyor
         self._element_err += 1 #self._element_err 1 arttırlıyor
         print('assignment error!') #ekrana yazılıyor
         self._head = self._Node(self._default, self._head) #eğer e 10'dan büyük ise yeni bir Node yaratılıyor, _Node sınıfı kullanılıyor, Node yaratılırken default değeri olarak -99 işleniyor, self._head elemannı next olarak aktarılıyor
         self._size += 1 #self._size 1 arttırılıyor
     else: #10'dan büyük değilse kullanılıyor
         self._head = self._Node(e, self._head) #eğer e 10'dan küçük ise yeni bir Node yaratılıyor, _Node sınıfı kullanılıyor, Node yaratılırken içeri hangi eleman girdiyse ("e") Yığın onunla açılıyor, self._head elemannı next olarak aktarılıyor
         self._size += 1 #self._size 1 arttırılıyor
"""
PUSH GENEL FONKSYON AÇIKLAMASI         
    eğer "e" değeri 10'dan büyükse yığına yeni bir bölge eklenerek başa -99 gelir
    eğer "e" değeri 10'dan küçük ise yığının başına "e" sayısı eklenir
"""    
     def top(self):#fonksyonu tanımlanıyor
         self._top_is_called += 1 #top fonksyonu her çağırıldığında self._top_is_called değeri 1 arttırılıyor
         if self.is_empty():#eğer self.is_empty kısmı doğruysa if'in içine gir
             print('Stack is empty')#ekrana basılır
         return self._head._element #top elementi geri dönüş değeri olarak veriliyor
     
        
     
        
     
        
"""
5/3
"""
"""
class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next' 
        def __init__(self, element, next):
            self._element = element
            self._next = next
    def __init__(self):
        """Create an empty queue."""
        self._tail = None 
        self._size = 0
"""
def first(self): #first fonksyonu tanımlanıyor
    if self.is_empty(): #.is_empty doğruysa if'in içine gir
        print('Queue is empty')#ekrana bas
        head = self._tail._next #yığının tepe noktasını kuyruktan sonraki elemana eşitliyoruz
    return head._element #yığının (top) noktasındaki elemanı return ediyoruz

def second(self): #second fonksyonu tanımlanıyor
    if self.is_empty(): # .is_empty doğru ise if'in içine gir
        raise Empty('Queue is empty') #"queue is empty" mesajı yükseltiliyor
    oldhead = self._tail._next #kuyruktan sonraki düğüm (ilk düğüm) oldhead değişkenine atanıyor
    if self._size == 1: #eğer kuyrukta 1 düğüm varsa
        self._tail = None #kuyruğun son düğümünü None'ye eşitle
    else:
        self._tail._next = oldhead._next #eğer kuyrukta 1'den fazla düğüm varsa tail.next değeri, listenin ilk düğümünden sonraki düğümü gösteriyor
    self._size -= 1
    return oldhead._element
