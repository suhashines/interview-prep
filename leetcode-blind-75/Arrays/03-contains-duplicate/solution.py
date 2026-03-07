def optimal(arr:list):
    
    """
    Time Complexity O(n)
    Space Complexity O(n)
    """
    
    st = set()
    
    for x in arr:
        if x in st:
            return True
        st.add(x)
    return False


print(optimal([1, 2, 3, 4]))