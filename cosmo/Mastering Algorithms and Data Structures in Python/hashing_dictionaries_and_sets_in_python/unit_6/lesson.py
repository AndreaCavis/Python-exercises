''' Problem 1: Frequent Words Finder

Let's start with an interesting task. Imagine being asked to construct a simple word frequency analyzer. 
Given a large body of text, we need to identify the three most frequently occurring words. 
Imagine working with large documents, such as news articles, thesis manuscripts, or even books. 
Identifying the most common words could give us an overview of the main themes or topics in the text.

Naive Approach:
An initial thought might be to iterate over the entire set of words, count each word's occurrences, and then compare the counts. 
However, this method would involve repetitive and redundant operations and is, therefore, inefficient. 
If we think back to the theory of computational complexity from our earlier lessons, 
this 'brute force' approach is known to have a time complexity of O(n^2), where n is the total number of words. 
That's not very appealing, right? Hence, we need to find an alternative approach that's more time-efficient.

Efficient Approach Explanation:
This is where Python dictionaries shine. A Python dictionary allows us to store data in key-value pairs. 
In this case, we can use each unique word in the text as a key and the frequency of the word as its corresponding value. 
As we traverse the document once, we can record the count of each word on the go, avoiding the need for multiple full-document checks. 
Hence, using a dictionary would drastically reduce our algorithm's time complexity and boost its efficiency. 

Solution Building:
Now, let's put this efficient approach into effect with some Python code and dive into its step-by-step explanation. '''

def frequent_words_finder(text: str) -> list:
    from collections import defaultdict

    text = text.lower()
    word_counts = defaultdict(int)
    word_list = text.split()

    for word in word_list:
        word_counts[word] += 1

    top_three = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    return [x[0]for x in top_three]



text = ''' Problem 1: Frequent Words Finder
Let's start with an interesting task. Imagine being asked to construct a simple word frequency analyzer. 
Given a large body of text, we need to identify the three most frequently occurring words. 
Imagine working with large documents, such as news articles, thesis manuscripts, or even books. 
Identifying the most common words could give us an overview of the main themes or topics in the text.
Naive Approach:
An initial thought might be to iterate over the entire set of words, count each word's occurrences, and then compare the counts. 
However, this method would involve repetitive and redundant operations and is, therefore, inefficient. 
If we think back to the theory of computational complexity from our earlier lessons, 
this 'brute force' approach is known to have a time complexity of O(n^2), where n is the total number of words. 
That's not very appealing, right? Hence, we need to find an alternative approach that's more time-efficient.
Efficient Approach Explanation:
This is where Python dictionaries shine. A Python dictionary allows us to store data in key-value pairs. 
In this case, we can use each unique word in the text as a key and the frequency of the word as its corresponding value. 
As we traverse the document once, we can record the count of each word on the go, avoiding the need for multiple full-document checks. 
Hence, using a dictionary would drastically reduce our algorithm's time complexity and boost its efficiency. 
Solution Building:
Now, let's put this efficient approach into effect with some Python code and dive into its step-by-step explanation. '''

print(frequent_words_finder(text))