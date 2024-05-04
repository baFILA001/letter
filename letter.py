# app.py
import streamlit as st

def main():
    st.title("Confession Letter")
    
    # Define the letter content
    letter_content = """
                                                                                                                                                    From 
                                                                                                                                                    Vikash Singh Bafila
                                                                                                                                                    Atgeir Intern,Batch-07
                                                                                                                                                    Apna PG,Somnath Nagar
                                                                                                                                                    Pune.

To Sejal Agarwal
Pune

Dear Sejal,

I am writing this letter to express my feelings that I have had for you since the first day I saw you in the office when Anand sir interviewed me, and after that, he brought me in to show the office.

At that time, I first saw you there, and I don't know, but it just felt different, which I hadn't felt before in my life. So during these three months of my internship, there are many inner virtues and qualities of yours that I observed, which are unique and I have never seen those before. So those are:

1. Intelligence: In my school and during my engineering studies, I observed that many girls were not proficient in practical tasks but excelled in theoretical concepts. However, in your case, I noticed that you are skilled in both practical work and theory, which is surprising and unique.

2. Generosity: During the internship and over the previous two weeks of project creation, I noticed that you were compassionate about helping others, and you were kind to them.

3. Humility: And the fact that you don't boast about your achievements is something I greatly admire, even if my batchmates may not see it the same way.

4. Forgiveness: During the internship, some of our batchmates used to mock you during online lectures, which I think you knew about, but despite that, you were kind to them and approached them to offer help.

And apart from the above-mentioned things that I have observed, there are many more aspects of your personality that I admire, but listing them all would make this letter too long.

So if you are in a relationship with someone, then sorry from my side as it is inappropriate, and I apologize for any inconvenience caused by my sharing, but I feel it's important to express. If I am not selected during our project review next Monday, I will return home with a clear mind and without any burden.

As it was my first time doing this type of thing, which I haven't done before because I haven't felt anything like this for anyone else before, so please forgive me.


Best regards,
Vikash Singh Bafila
"""
    
    # Display the letter
    st.text_area("", value=letter_content, height=1100)

if __name__ == "__main__":
    main()
