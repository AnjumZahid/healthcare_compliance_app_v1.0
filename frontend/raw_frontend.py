# # frontend.py
# import streamlit as st
# import requests

# st.set_page_config(page_title="FDA Compliance Checker", layout="wide")

# # Sidebar: File Uploads
# st.sidebar.header("Upload Patient Files")
# uploaded_pdf = st.sidebar.file_uploader("Choose Patient History PDF", type=["pdf"])
# uploaded_img = st.sidebar.file_uploader("Upload X-ray Image", type=["png", "jpg", "jpeg"])

# # Medicines input
# st.header("Enter Medicines (comma separated)")
# medicine_text = st.text_area("Medicines", "Amoxicillin, Paracetamol, Metformin")

# if st.button("Run Compliance Check"):
#     if uploaded_pdf and uploaded_img and medicine_text:
#         with st.spinner("⚙️ Running compliance check... please wait..."):
#             try:
#                 # Send files + medicine_text to backend
#                 files = {
#                     "file": uploaded_pdf,
#                     "image": uploaded_img
#                 }
#                 data = {"medicine_text": medicine_text}

#                 response = requests.post("http://127.0.0.1:8000/process/", files=files, data=data)

#                 if response.status_code == 200:
#                     result = response.json()

#                     st.subheader("✅ Generated Compliance Questions")
#                     st.json(result["questions"])

#                     st.subheader("📄 Retrieved Context")
#                     st.write(result["context"])

#                     st.subheader("🩻 Image Classification")
#                     st.write(result.get("image_text", "No image processed."))

#                     st.subheader("🔎 Compliance Query")
#                     st.write(result["compliance_query"])

#                     st.subheader("⚖️ Compliance Answer")
#                     st.write(result["compliance_answer"])
#                 else:
#                     st.error("❌ Error from backend: " + str(response.text))
#             except Exception as e:
#                 st.error(f"⚠️ Request failed: {e}")
#     else:
#         st.warning("⚠️ Please upload both PDF + Image and enter medicine names.")

# # streamlit run frontend/frontend.py


# ================================

# ## frontend.py
# import streamlit as st
# import requests
# from streamlit_tags import st_tags  # pip install streamlit-tags

# st.set_page_config(page_title="FDA Compliance Checker", layout="wide")

# # --- Medicines input (tag style) ---
# st.header("Enter Medicines")
# medicines = st_tags(
#     label="💊 Add Medicines",
#     text="Type medicine and press Enter",
#     value=["Amoxicillin", "Paracetamol"],
#     suggestions=["Metformin", "Ibuprofen", "Azithromycin", "Ciprofloxacin"],
#     maxtags=50,
# )

# st.subheader("➕ Add Custom Compliance Questions")
# doctor_questions = st_tags(
#     label="Type a question and press Enter (you can add many)",
#     text="Type question and press Enter",
#     value=[],
#     suggestions=[],
#     maxtags=50,
# )

# # Show them vertically as preview
# if doctor_questions:
#     st.write("📋 Your entered questions:")
#     for q in doctor_questions:
#         st.write(f"- {q}")


# # --- Run button ---
# if st.button("Run Compliance Check"):
#     if medicines:
#         with st.spinner("⚙️ Running compliance check..."):
#             try:
#                 medicine_text = ", ".join(medicines)

#                 # Dummy placeholders for now (so you don't need file upload)
#                 dummy_pdf_text = "Dummy patient history: diabetic, hypertension, 45 years old."
#                 dummy_img_text = "Dummy X-ray classification: No major abnormality."

#                 payload = {
#                     "medicine_text": medicine_text,
#                     "doctor_questions": doctor_questions,   # list of questions
#                     "pdf_text": dummy_pdf_text,
#                     "image_text": dummy_img_text,
#                 }

#                 resp = requests.post("http://127.0.0.1:8000/process/", json=payload, timeout=10)

#                 if resp.status_code == 200:
#                     result = resp.json()

#                     st.subheader("✅ Generated Compliance Questions")
#                     st.json(result["questions"])
#                 else:
#                     st.error("❌ Error from backend: " + resp.text)
#             except Exception as e:
#                 st.error(f"⚠️ Request failed: {e}")
#     else:
#         st.warning("⚠️ Please enter at least one medicine.")



# =================================================

# ## frontend.py
# import streamlit as st
# import requests
# import json
# from streamlit_tags import st_tags  # pip install streamlit-tags
# import urllib.parse

# st.set_page_config(page_title="FDA Compliance Checker", layout="wide")

# # --- Medicines input (tag style) ---
# st.header("Enter Medicines")
# medicines = st_tags(
#     label="💊 Add Medicines",
#     text="Type medicine and press Enter",
#     value=["Amoxicillin", "Paracetamol"],
#     suggestions=["Metformin", "Ibuprofen", "Azithromycin", "Ciprofloxacin"],
#     maxtags=50,
# )

# st.subheader("➕ Add Custom Compliance Questions")
# doctor_questions = st_tags(
#     label="Type a question and press Enter (you can add many)",
#     text="Type question and press Enter",
#     value=[],
#     suggestions=[],
#     maxtags=50,
# )

# # Show them vertically as preview
# if doctor_questions:
#     st.write("📋 Your entered questions:")
#     for q in doctor_questions:
#         st.write(f"- {q}")

# # --- Run button ---
# if st.button("Generate Complince Question"):
#     if medicines:
#         with st.spinner("⚙️ Generating Complince Question..."):
#             try:
#                 medicine_text = ", ".join(medicines)

#                 # Dummy placeholders for now
#                 dummy_pdf_text = "Dummy patient history: diabetic, hypertension, 45 years old."
#                 dummy_img_text = "Dummy X-ray classification: No major abnormality."

#                 payload = {
#                     "medicine_text": medicine_text,
#                     "doctor_questions": doctor_questions,   # list of questions
#                     "pdf_text": dummy_pdf_text,
#                     "image_text": dummy_img_text,
#                 }

#                 resp = requests.post("http://127.0.0.1:8000/process/", json=payload, timeout=10)

#                 if resp.status_code == 200:
#                     result = resp.json()

#                     # ✅ Show success message instead of printing questions
#                     # st.success("✅ Compliance questions generated successfully!")

#                     # Create a JSON string to view in new tab/window
                    
#                     questions_json = json.dumps(result["questions"], indent=2)
#                     # After getting result from backend
#                     questions = result["questions"]

#                     # Show success message
#                     st.success("✅ Compliance questions generated successfully!")

#                     # Collapsible view for generated questions
#                     with st.expander("View Generated Questions"):
#                         for q in questions:
#                             st.write(f"- {q}")
                    
#                 else:
#                     st.error("❌ Error from backend: " + resp.text)
#             except Exception as e:
#                 st.error(f"⚠️ Request failed: {e}")
#     else:
#         st.warning("⚠️ Please enter at least one medicine.")

# ================================

# ## frontend.py
# import streamlit as st
# import requests
# from streamlit_tags import st_tags  # pip install streamlit-tags

# st.set_page_config(page_title="FDA Compliance Checker", layout="wide")

# # --- Medicines input (tag style) ---
# st.header("Enter Medicines")
# medicines = st_tags(
#     label="💊 Add Medicines",
#     text="Type medicine and press Enter",
#     value=["Amoxicillin", "Paracetamol"],
#     suggestions=["Metformin", "Ibuprofen", "Azithromycin", "Ciprofloxacin"],
#     maxtags=50,
# )

# st.subheader("➕ Add Custom Compliance Questions")
# doctor_questions = st_tags(
#     label="Type a question and press Enter (you can add many)",
#     text="Type question and press Enter",
#     value=[],
#     suggestions=[],
#     maxtags=50,
# )

# # Show entered custom questions
# if doctor_questions:
#     st.write("📋 Your entered questions:")
#     for q in doctor_questions:
#         st.write(f"- {q}")

# # --- Run button ---
# if st.button("Generate Compliance Questions"):
#     if medicines:
#         with st.spinner("⚙️ Generating Compliance Questions..."):
#             try:
#                 medicine_text = ", ".join(medicines)

#                 # Dummy placeholders
#                 dummy_pdf_text = "Dummy patient history: diabetic, hypertension, 45 years old."
#                 dummy_img_text = "Dummy X-ray classification: No major abnormality."

#                 # --- Prepare payload ---
#                 payload = {
#                     "medicine_text": medicine_text,
#                     "doctor_questions": doctor_questions,
#                     "pdf_text": dummy_pdf_text,
#                     "image_text": dummy_img_text,
#                 }

#                 # --- Send request to backend ---
#                 resp = requests.post("http://127.0.0.1:8000/process/", json=payload, timeout=10)

#                 if resp.status_code == 200:
#                     result = resp.json()
#                     generated_prompt = result["prompt"]
#                     questions = result["questions"]

#                     # ✅ Success message
#                     st.success("✅ Compliance questions generated successfully!")

#                     # --- Collapsible section: Generated Prompt ---
#                     with st.expander("View Generated Prompt"):
#                         st.code(generated_prompt, language="text")

#                     # --- Collapsible section: Generated Questions ---
#                     with st.expander("View Generated Questions"):
#                         for i, q in enumerate(questions, start=1):
#                             st.write(f"{i}. {q}")

#                 else:
#                     st.error("❌ Error from backend: " + resp.text)

#             except Exception as e:
#                 st.error(f"⚠️ Request failed: {e}")
#     else:
#         st.warning("⚠️ Please enter at least one medicine.")


# ================================

# import streamlit as st
# import requests
# from streamlit_tags import st_tags  # pip install streamlit-tags

# st.set_page_config(page_title="FDA Compliance Checker", layout="wide")

# # --- Medicines input ---
# st.header("Enter Medicines")
# medicines = st_tags(
#     label="💊 Add Medicines",
#     text="Type medicine and press Enter",
#     value=["Amoxicillin", "Paracetamol"],
#     suggestions=["Metformin", "Ibuprofen", "Azithromycin", "Ciprofloxacin"],
#     maxtags=50,
# )

# st.subheader("➕ Add Custom Compliance Questions")
# doctor_questions = st_tags(
#     label="Type a question and press Enter (you can add many)",
#     text="Type question and press Enter",
#     value=[],
#     suggestions=[],
#     maxtags=50,
# )

# # Preview custom questions
# if doctor_questions:
#     st.write("📋 Your entered questions:")
#     for q in doctor_questions:
#         st.write(f"- {q}")

# # --- Run button ---
# if st.button("Generate Compliance Questions"):
#     if medicines:
#         with st.spinner("⚙️ Generating Compliance Questions..."):
#             try:
#                 medicine_text = ", ".join(medicines)
#                 dummy_pdf_text = "Dummy patient history: diabetic, hypertension, 45 years old."
#                 dummy_img_text = "Dummy X-ray classification: No major abnormality."

#                 payload = {
#                     "medicine_text": medicine_text,
#                     "doctor_questions": doctor_questions,
#                     "pdf_text": dummy_pdf_text,
#                     "image_text": dummy_img_text,
#                 }

#                 resp = requests.post("http://127.0.0.1:8000/process/", json=payload, timeout=10)

#                 if resp.status_code == 200:
#                     result = resp.json()
#                     generated_prompt = result["prompt"]
#                     questions = result["questions"]
#                     retrieved_chunks = result["retrieved_chunks"]

#                     st.success("✅ Compliance questions generated successfully!")

#                     # --- Collapsible: Generated Prompt ---
#                     with st.expander("View Generated Prompt"):
#                         st.code(generated_prompt, language="text")

#                     # --- Collapsible: Questions with retrieved chunks ---
#                     with st.expander("View Generated Questions and Retrieved Chunks"):
#                         for i, q in enumerate(questions, start=1):
#                             with st.expander(f"{i}. {q}"):
#                                 chunks = retrieved_chunks.get(q, [])
#                                 for j, chunk in enumerate(chunks, start=1):
#                                     st.write(f"- {chunk}")

#                 else:
#                     st.error("❌ Error from backend: " + resp.text)

#             except Exception as e:
#                 st.error(f"⚠️ Request failed: {e}")
#     else:
#         st.warning("⚠️ Please enter at least one medicine.")


# ==============================================

# import streamlit as st
# import requests
# from streamlit_tags import st_tags  # pip install streamlit-tags

# st.set_page_config(page_title="FDA Compliance Checker", layout="wide")

# # --- Medicines input ---
# st.header("Enter Medicines")
# medicines = st_tags(
#     label="💊 Add Medicines",
#     text="Type medicine and press Enter",
#     value=["Amoxicillin", "Paracetamol"],
#     suggestions=["Metformin", "Ibuprofen", "Azithromycin", "Ciprofloxacin"],
#     maxtags=50,
# )

# st.subheader("➕ Add Custom Compliance Questions")
# doctor_questions = st_tags(
#     label="Type a question and press Enter (you can add many)",
#     text="Type question and press Enter",
#     value=[],
#     suggestions=[],
#     maxtags=50,
# )

# # Preview custom questions
# if doctor_questions:
#     st.write("📋 Your entered questions:")
#     for q in doctor_questions:
#         st.write(f"- {q}")

# # --- Run button ---
# if st.button("Generate Compliance Questions"):
#     if medicines:
#         with st.spinner("⚙️ Generating Compliance Questions..."):
#             try:
#                 medicine_text = ", ".join(medicines)
#                 dummy_pdf_text = "Dummy patient history: diabetic, hypertension, 45 years old."
#                 dummy_img_text = "Dummy X-ray classification: No major abnormality."

#                 payload = {
#                     "medicine_text": medicine_text,
#                     "doctor_questions": doctor_questions,
#                     "pdf_text": dummy_pdf_text,
#                     "image_text": dummy_img_text,
#                 }

#                 resp = requests.post("http://127.0.0.1:8000/process/", json=payload, timeout=10)

#                 if resp.status_code == 200:
#                     result = resp.json()
#                     generated_prompt = result["prompt"]
#                     questions = result["questions"]
#                     retrieved_chunks = result["retrieved_chunks"]
#                     fda_info = result["fda_info"]

#                     st.success("✅ Compliance questions generated successfully!")

#                     # --- Collapsible: Generated Prompt ---
#                     with st.expander("View Generated Prompt"):
#                         st.code(generated_prompt, language="text")

#                     # --- Collapsible: Questions with retrieved chunks ---
#                     with st.expander("View Generated Questions and Retrieved Chunks"):
#                         for i, q in enumerate(questions, start=1):
#                             with st.expander(f"{i}. {q}"):
#                                 chunks = retrieved_chunks.get(q, [])
#                                 for j, chunk in enumerate(chunks, start=1):
#                                     st.write(f"- {chunk}")

#                     # --- Collapsible: FDA Info ---
#                     with st.expander("📜 FDA Information"):
#                         for med, info in fda_info.items():
#                             with st.expander(med):
#                                 st.write(info)

#                 else:
#                     st.error("❌ Error from backend: " + resp.text)

#             except Exception as e:
#                 st.error(f"⚠️ Request failed: {e}")
#     else:
#         st.warning("⚠️ Please enter at least one medicine.")


# ===========================================

# import streamlit as st
# import requests
# from streamlit_tags import st_tags  # pip install streamlit-tags

# st.set_page_config(page_title="FDA Compliance Checker", layout="wide")

# # --- Medicines input ---
# st.header("Enter Medicines")
# medicines = st_tags(
#     label="💊 Add Medicines",
#     text="Type medicine and press Enter",
#     value=["Amoxicillin", "Paracetamol"],
#     suggestions=["Metformin", "Ibuprofen", "Azithromycin", "Ciprofloxacin"],
#     maxtags=50,
# )

# st.subheader("➕ Add Custom Compliance Questions")
# doctor_questions = st_tags(
#     label="Type a question and press Enter (you can add many)",
#     text="Type question and press Enter",
#     value=[],
#     suggestions=[],
#     maxtags=50,
# )

# # Preview custom questions
# if doctor_questions:
#     st.write("📋 Your entered questions:")
#     for q in doctor_questions:
#         st.write(f"- {q}")

# # --- Run button ---
# if st.button("Generate Compliance Questions"):
#     if medicines:
#         with st.spinner("⚙️ Generating Compliance Questions..."):
#             try:
#                 medicine_text = ", ".join(medicines)
#                 dummy_pdf_text = "Dummy patient history: diabetic, hypertension, 45 years old."
#                 dummy_img_text = "Dummy X-ray classification: No major abnormality."

#                 payload = {
#                     "medicine_text": medicine_text,
#                     "doctor_questions": doctor_questions,
#                     "pdf_text": dummy_pdf_text,
#                     "image_text": dummy_img_text,
#                 }

#                 resp = requests.post("http://127.0.0.1:8000/process/", json=payload, timeout=10)

#                 if resp.status_code == 200:
#                     result = resp.json()
#                     generated_prompt = result["prompt"]
#                     questions = result["questions"]
#                     retrieved_chunks = result["retrieved_chunks"]
#                     fda_info = result["fda_info"]
#                     final_prompt = result["final_prompt"]

#                     st.success("✅ Compliance questions generated successfully!")

#                     # --- Collapsible: Generated Prompt ---
#                     with st.expander("View Generated Prompt"):
#                         st.code(generated_prompt, language="text")

#                     # --- Collapsible: Questions + Retrieved Chunks ---
#                     with st.expander("View Generated Questions and Retrieved Chunks"):
#                         for i, q in enumerate(questions, start=1):
#                             with st.expander(f"{i}. {q}"):
#                                 chunks = retrieved_chunks.get(q, [])
#                                 for j, chunk in enumerate(chunks, start=1):
#                                     st.write(f"- {chunk}")

#                     # --- Collapsible: FDA Info ---
#                     with st.expander("📜 FDA Information"):
#                         for med, info in fda_info.items():
#                             with st.expander(med):
#                                 st.write(info)

#                     # --- Collapsible: Final Compliance Prompt ---
#                     with st.expander("📝 Final Compliance Prompt"):
#                         st.code(final_prompt, language="text")

#                 else:
#                     st.error("❌ Error from backend: " + resp.text)

#             except Exception as e:
#                 st.error(f"⚠️ Request failed: {e}")
#     else:
#         st.warning("⚠️ Please enter at least one medicine.")

# ======================================

# import streamlit as st
# import requests
# from streamlit_tags import st_tags  # pip install streamlit-tags


# st.set_page_config(page_title="FDA Compliance Checker", layout="wide")

# # --- Medicines input ---
# st.header("Enter Medicines")
# medicines = st_tags(
#     label="💊 Add Medicines",
#     text="Type medicine and press Enter",
#     value=["Amoxicillin", "Paracetamol"],
#     suggestions=["Metformin", "Ibuprofen", "Azithromycin", "Ciprofloxacin"],
#     maxtags=50,
# )

# st.subheader("➕ Add Custom Compliance Questions")
# doctor_questions = st_tags(
#     label="Type a question and press Enter (you can add many)",
#     text="Type question and press Enter",
#     value=[],
#     suggestions=[],
#     maxtags=50,
# )

# # Preview custom questions
# if doctor_questions:
#     st.write("📋 Your entered questions:")
#     for q in doctor_questions:
#         st.write(f"- {q}")

# # --- Run button ---
# if st.button("Generate Compliance Questions"):
#     if medicines:
#         with st.spinner("⚙️ Generating Compliance Questions..."):
#             try:
#                 medicine_text = ", ".join(medicines)
#                 dummy_pdf_text = "Dummy patient history: diabetic, hypertension, 45 years old."
#                 dummy_img_text = "Dummy X-ray classification: No major abnormality."

#                 payload = {
#                     "medicine_text": medicine_text,
#                     "doctor_questions": doctor_questions,
#                     "pdf_text": dummy_pdf_text,
#                     "image_text": dummy_img_text,
#                 }

#                 resp = requests.post("http://127.0.0.1:8000/process/", json=payload, timeout=10)

#                 if resp.status_code == 200:
#                     result = resp.json()

#                     generated_prompt = result["prompt"]
#                     questions = result["questions"]
#                     retrieved_chunks = result["retrieved_chunks"]
#                     fda_info = result["fda_info"]
#                     final_prompt = result["final_prompt"]
#                     final_answer = result["final_answer"]

#                     st.success("✅ Compliance flow completed successfully!")

#                     # --- Collapsible: Generated Prompt ---
#                     with st.expander("View Generated Prompt"):
#                         st.code(generated_prompt, language="text")

#                     # --- Collapsible: Questions + Retrieved Chunks ---
#                     with st.expander("View Generated Questions and Retrieved Chunks"):
#                         for i, q in enumerate(questions, start=1):
#                             with st.expander(f"{i}. {q}"):
#                                 chunks = retrieved_chunks.get(q, [])
#                                 for j, chunk in enumerate(chunks, start=1):
#                                     st.write(f"- {chunk}")

#                     # --- Collapsible: FDA Info ---
#                     with st.expander("📜 FDA Information"):
#                         for med, info in fda_info.items():
#                             with st.expander(med):
#                                 st.write(info)

#                     # --- Collapsible: Final Compliance Prompt ---
#                     with st.expander("📝 Final Compliance Prompt"):
#                         st.code(final_prompt, language="text")

#                     # --- Final Answer (always visible, styled) ---
#                     st.markdown("### 🏥 Final Compliance Answer")
#                     st.info(final_answer)

#                 else:
#                     st.error("❌ Error from backend: " + resp.text)

#             except Exception as e:
#                 st.error(f"⚠️ Request failed: {e}")
#     else:
#         st.warning("⚠️ Please enter at least one medicine.")

# ==========================================

# import streamlit as st
# import requests
# from streamlit_tags import st_tags  # pip install streamlit-tags
# import time

# st.set_page_config(page_title="FDA Compliance Checker", layout="wide")

# # --- Medicines input ---
# st.header("Enter Medicines")
# medicines = st_tags(
#     label="💊 Add Medicines",
#     text="Type medicine and press Enter",
#     value=["Amoxicillin", "Paracetamol"],
#     suggestions=["Metformin", "Ibuprofen", "Azithromycin", "Ciprofloxacin"],
#     maxtags=50,
# )

# st.subheader("➕ Add Custom Compliance Questions")
# doctor_questions = st_tags(
#     label="Type a question and press Enter (you can add many)",
#     text="Type question and press Enter",
#     value=[],
#     suggestions=[],
#     maxtags=50,
# )

# # Preview custom questions
# if doctor_questions:
#     st.write("📋 Your entered questions:")
#     for q in doctor_questions:
#         st.write(f"- {q}")

# # --- Run button ---
# if st.button("Generate Compliance Questions"):
#     if medicines:
#         try:
#             medicine_text = ", ".join(medicines)
#             dummy_pdf_text = "Dummy patient history: diabetic, hypertension, 45 years old."
#             dummy_img_text = "Dummy X-ray classification: No major abnormality."

#             payload = {
#                 "medicine_text": medicine_text,
#                 "doctor_questions": doctor_questions,
#                 "pdf_text": dummy_pdf_text,
#                 "image_text": dummy_img_text,
#             }

#             with st.spinner("⚙️ Generating Compliance Questions..."):
#                 resp = requests.post("http://127.0.0.1:8000/process/", json=payload, timeout=10)
#                 time.sleep(3)  # simulate slow API

#             if resp.status_code == 200:
#                 result = resp.json()

#                 generated_prompt = result["prompt"]
#                 questions = result["questions"]
#                 retrieved_chunks = result["retrieved_chunks"]
#                 fda_info = result["fda_info"]
#                 final_prompt = result["final_prompt"]
#                 final_answer = result["final_answer"]

#                 st.success("✅ Compliance flow completed successfully!")

#                 with st.spinner("✍️ Preparing Generated Prompt..."):
#                     time.sleep(3)
#                     with st.expander("View Generated Prompt"):
#                         st.code(generated_prompt, language="text")

#                 with st.spinner("🔎 Preparing Questions and Retrieved Chunks..."):
#                     time.sleep(3)
#                     with st.expander("View Generated Questions and Retrieved Chunks"):
#                         for i, q in enumerate(questions, start=1):
#                             with st.expander(f"{i}. {q}"):
#                                 chunks = retrieved_chunks.get(q, [])
#                                 for j, chunk in enumerate(chunks, start=1):
#                                     st.write(f"- {chunk}")

#                 with st.spinner("📖 Fetching FDA Information..."):
#                     time.sleep(3)
#                     with st.expander("📜 FDA Information"):
#                         for med, info in fda_info.items():
#                             with st.expander(med):
#                                 st.write(info)

#                 with st.spinner("⚙️ Building Final Compliance Prompt..."):
#                     time.sleep(3)
#                     with st.expander("📝 Final Compliance Prompt"):
#                         st.code(final_prompt, language="text")

#                 with st.spinner("🤖 Generating Final Compliance Answer..."):
#                     time.sleep(3)
#                     st.markdown("### 🏥 Final Compliance Answer")
#                     st.info(final_answer)

#             else:
#                 st.error("❌ Error from backend: " + resp.text)

#         except Exception as e:
#             st.error(f"⚠️ Request failed: {e}")
#     else:
#         st.warning("⚠️ Please enter at least one medicine.")


# ==================================================