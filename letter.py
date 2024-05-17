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

To xyz
Pune

Dear Mam,

I am writing this letter to express my feelings that I have had for you since the first day I saw you when you where shifting your luggage into that flat which is in front of our pg.

At that time, I first saw you there, and I don't know, but it just felt different, which I hadn't felt before in my life. So during these months, there are many inner virtues and qualities of yours that I observed, which are unique and I have never seen those before. So those are:

1. Integrity: I admire your integrity, as you stay true to yourself. I have observed that you do what you feel is right and what you want, without feeling ashamed of others' opinions.

2. Independence: As what I've observed, you navigate through life with a remarkable sense of independence.Your independence isn't just about doing things on your own; it's about having the courage to follow your heart and the resilience to stand tall amidst uncertainties. 

3. Serene: I thing you have a serene demeanor and the calm and tranquil presence you exude in any situation is remarkable. Your ability to remain composed and peaceful, even amidst chaos, is truly remarkable and something I deeply admire about you.

4. Radiant Personality and Beauty: You are beautiful, but from our second floor, I can only see your hair, which is even more stunning.

And apart from the above-mentioned things that I have observed, there are many more aspects of your personality that I admire, but listing them all would make this letter too long.

So if you are in a relationship with someone, then sorry from my side as it is inappropriate, and I apologize for any inconvenience caused by my sharing, but I feel it's important to express. Because On Monday, I will be assigned to my project group, and I wanted to express my feelings to you so that I can start my project work with a clear mind and without any burden.

As it was my first time doing this type of thing, which I haven't done before because I haven't felt anything like this for anyone else before, so please forgive me.

I'm sorry for not mentioning your name, as I don't know it or much about you. However, I'm interested in learning more about you. If you're comfortable, feel free to communicate with me via email at vikashbafila321@gmail.com. If you find my approach inappropriate, I apologize and assure you that I won't do anything similar in the future.

Best regards,
Vikash Singh Bafila
"""
    
    # Display the letter
    st.text_area("", value=letter_content, height=1500)

if __name__ == "__main__":
    main()
