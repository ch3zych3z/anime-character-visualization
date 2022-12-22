import streamlit as st
import api


def main():
    with st.form("visualizing_form"):
        st.title("Visualize character in your favourite anime style by description")
        description = st.text_input("Character description", max_chars=1024, placeholder="Big boy")
        title = st.text_input("Anime title", max_chars=128, placeholder="Tokyo ghoul")
        submitted = st.form_submit_button("Visualize")
        if submitted:
            response = api.visualize_query(description=description, title=title)
            if response.status_code == 200:
                st.image(image=response.content, output_format="JPEG")
            else:
                st.text("Sorry, service unavailable. Try again later :(")


if __name__ == "__main__":
    main()
