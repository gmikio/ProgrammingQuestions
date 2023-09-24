class MaxHeap:
    def __init__(self):
        # Inicializa a lista que será usada para armazenar os elementos da max heap.
        self.heap = []

    def insert(self, value):
        # Insere um valor na max heap.
        self.heap.append(value)  # Adiciona o valor ao final da lista.
        self._heapify_up(len(self.heap) - 1)  # Chama o método _heapify_up para manter a propriedade da max heap.

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Remove e retorna o elemento máximo (a raiz da max heap).
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Substitui a raiz pelo último elemento.
        self._heapify_down(0)  # Chama o método _heapify_down para manter a propriedade da max heap.
        return max_value

    def _heapify_up(self, index):
        # Mantém a propriedade da max heap após a inserção.
        while index > 0:
            parent_index = (index - 1) // 2  # Calcula o índice do pai.
            if self.heap[parent_index] < self.heap[index]:
                # Se o valor do pai for menor que o valor atual, troca os elementos.
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index  # Move para o índice do pai.
            else:
                break  # Se a propriedade da max heap estiver satisfeita, pare.

    def _heapify_down(self, index):
        # Mantém a propriedade da max heap após a remoção.
        while True:
            left_child_index = 2 * index + 1  # Calcula o índice do filho esquerdo.
            right_child_index = 2 * index + 2  # Calcula o índice do filho direito.
            largest = index  # Inicialmente, assume-se que o índice atual é o maior.

            if (
                left_child_index < len(self.heap)
                and self.heap[left_child_index] > self.heap[largest]
            ):
                # Se o filho esquerdo for maior que o índice atual, atualiza o índice do maior.
                largest = left_child_index

            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] > self.heap[largest]
            ):
                # Se o filho direito for maior que o índice atual ou o filho esquerdo,
                # atualiza o índice do maior.
                largest = right_child_index

            if largest != index:
                # Se o maior valor não estiver no índice atual, troca os elementos.
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest  # Move para o índice do maior filho.
            else:
                break  # Se a propriedade da max heap estiver satisfeita, pare.

def find_kth_maximum(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None

    max_heap = MaxHeap()
    for num in arr:
