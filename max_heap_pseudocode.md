
Class MaxHeap:
    HeapArray

    Function get_max():
        If HeapArray is empty:
            Raise Exception
        Return HeapArray[0]

    Function insert(Value):
        Append Value to HeapArray
        Index = size(HeapArray) - 1

        While Index > 0:
            Parent = (Index - 1) // 2
            If HeapArray[Index] > HeapArray[Parent]:
                Swap HeapArray[Index], HeapArray[Parent]
                Index = Parent
            Else:
                Break

    Function extract_max():
        If HeapArray is empty:
            Raise Exception

        MaxValue = HeapArray[0]
        HeapArray[0] = HeapArray[last]
        Remove last element

        Index = 0
        Size = size(HeapArray)

        While True:
            Largest = Index
            Left = 2 * Index + 1
            Right = 2 * Index + 2

            If Left < Size and HeapArray[Left] > HeapArray[Largest]:
                Largest = Left
            If Right < Size and HeapArray[Right] > HeapArray[Largest]:
                Largest = Right

            If Largest != Index:
                Swap HeapArray[Index], HeapArray[Largest]
                Index = Largest
            Else:
                Break

        Return MaxValue
