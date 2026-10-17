<h1 align="center">Saksham Boldhan</h1>

<p align="center">
  Full-stack developer building web apps with machine learning behind them.<br/>
  Third-year B.Tech, AI &amp; Data Science · Ramdeobaba University
</p>

<p align="center">
  <a href="https://sakshamboldhan.vercel.app"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-sakshamboldhan.vercel.app-1f2937?style=flat-square&logo=vercel&logoColor=white"></a>
  <a href="https://github.com/saksham999-SAK"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-saksham999--SAK-1f2937?style=flat-square&logo=github&logoColor=white"></a>
  <!-- Uncomment and fill in once you confirm the links:
  <a href="https://www.linkedin.com/in/YOUR-HANDLE"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-connect-1f2937?style=flat-square&logo=linkedin&logoColor=white"></a>
  <a href="mailto:YOUR-EMAIL"><img alt="Email" src="https://img.shields.io/badge/Email-get_in_touch-1f2937?style=flat-square&logo=gmail&logoColor=white"></a>
  -->
</p>

---

## About

I'm a third-year B.Tech student specialising in AI and Data Science. I like projects where a model or data pipeline sits behind an interface people can actually use: an API that scores EV battery health, a habit tracker that turns daily choices into CO₂ numbers, a website for a run club.

Right now I'm building **Strivioco**, a community platform that connects runners with running clubs and events, while strengthening my ML and deep learning fundamentals alongside it.

---

## Featured projects

### EV Battery Intelligence
Machine-learning system for lithium-ion battery health. It outputs **State of Health (SOH)**, **Remaining Useful Life (RUL)** and an **anomaly status**.

- Three scikit-learn models trained in Colab and exported with joblib; a **FastAPI** service loads them and serves predictions with auto-generated interactive API docs.
- Training and serving are separate: the feature-column list ships with the models so inference uses the same input schema as training.
- TypeScript frontend deployed on Vercel. SHAP is part of the backend stack for explaining predictions.

`Python` `FastAPI` `scikit-learn` `pandas` `SHAP` `TypeScript`

[Repository](https://github.com/saksham999-SAK/EV-Battery-Intelligence) · [Live demo](https://frontend-ten-sage-xr96sb4oys.vercel.app)

### Eco-Commit AI
Full-stack sustainability tracker. Users log eco-friendly actions (walking, cycling, public transport, skipping the AC), and the backend turns each one into kg of CO₂ saved, eco-points and streaks, with AI-generated recommendations and campus / city / state / country leaderboards. Built with a team for a GDG Nagpur problem statement.

- REST API on **FastAPI** with **SQLAlchemy** and a PostgreSQL driver, JWT authentication, bcrypt password hashing and Pydantic validation.
- Backend tests with pytest; frontend and backend live in one repo and deploy through Vercel.

`Python` `FastAPI` `SQLAlchemy` `PostgreSQL` `JWT` `pytest`

[Repository](https://github.com/saksham999-SAK/PS2_gdgnagpur_Teamhackit) · [Live demo](https://ps-2-gdgnagpur-teamhackit.vercel.app)

### NextWord AI
Type a sentence and a trained **LSTM** neural network predicts the next word, wrapped in a web app so the model can be tried straight from the browser.

`JavaScript` `LSTM` `Deep Learning`

[Repository](https://github.com/saksham999-SAK/next_word) · [Live demo](https://next-word-bice.vercel.app)

### Raftaar Run Club
Website for a run club: upcoming runs, merchandise and member benefits. Built with React and Vite, and a practical step toward the community-platform work in Strivioco.

`React` `Vite` `JavaScript`

[Repository](https://github.com/saksham999-SAK/raftaarClub) · [Live site](https://raftaar-club.vercel.app)

---

## Tech stack

**Languages**<br/>
<img alt="Python" src="https://img.shields.io/badge/Python-1f2937?style=flat-square&logo=python&logoColor=white"> <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-1f2937?style=flat-square&logo=javascript&logoColor=white"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-1f2937?style=flat-square&logo=typescript&logoColor=white"> <img alt="Java" src="https://img.shields.io/badge/Java-1f2937?style=flat-square&logo=openjdk&logoColor=white"> <img alt="HTML5" src="https://img.shields.io/badge/HTML5-1f2937?style=flat-square&logo=html5&logoColor=white"> <img alt="CSS3" src="https://img.shields.io/badge/CSS3-1f2937?style=flat-square&logo=css3&logoColor=white">

**Frontend**<br/>
<img alt="React" src="https://img.shields.io/badge/React-1f2937?style=flat-square&logo=react&logoColor=white"> <img alt="Vite" src="https://img.shields.io/badge/Vite-1f2937?style=flat-square&logo=vite&logoColor=white">

**Backend and databases**<br/>
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-1f2937?style=flat-square&logo=fastapi&logoColor=white"> <img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-1f2937?style=flat-square&logo=sqlalchemy&logoColor=white"> <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-1f2937?style=flat-square&logo=postgresql&logoColor=white"> <img alt="pytest" src="https://img.shields.io/badge/pytest-1f2937?style=flat-square&logo=pytest&logoColor=white">

**ML and data**<br/>
<img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-1f2937?style=flat-square&logo=scikitlearn&logoColor=white"> <img alt="pandas" src="https://img.shields.io/badge/pandas-1f2937?style=flat-square&logo=pandas&logoColor=white"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-1f2937?style=flat-square&logo=numpy&logoColor=white"> <img alt="SciPy" src="https://img.shields.io/badge/SciPy-1f2937?style=flat-square&logo=scipy&logoColor=white"> <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-1f2937?style=flat-square&logo=jupyter&logoColor=white"> <img alt="Google Colab" src="https://img.shields.io/badge/Google_Colab-1f2937?style=flat-square&logo=googlecolab&logoColor=white">

**Tools and deployment**<br/>
<img alt="Git" src="https://img.shields.io/badge/Git-1f2937?style=flat-square&logo=git&logoColor=white"> <img alt="GitHub" src="https://img.shields.io/badge/GitHub-1f2937?style=flat-square&logo=github&logoColor=white"> <img alt="Vercel" src="https://img.shields.io/badge/Vercel-1f2937?style=flat-square&logo=vercel&logoColor=white">

---

## Experience

**Website redesign · RCOEM TBI**
Redesigned the RCOEM TBI website in HTML and CSS, rebuilding the Home page and the E-Cell page from scratch. [Repository](https://github.com/saksham999-SAK/Saksham-s-TBI_WEBSITE)

<!-- Add internships, internal projects and leadership roles from your resume here, in the same format:
**Role · Organisation**
One or two lines on what you built or led.
-->

---

## Currently exploring

- Deep learning beyond LSTMs, and getting trained models into usable web products
- Data analysis and ML fundamentals ([AIML_PRACTICE](https://github.com/saksham999-SAK/AIML_PRACTICE), [data-analysis-study-](https://github.com/saksham999-SAK/data-analysis-study-))
- Data structures and algorithms in Java ([dsa-journney](https://github.com/saksham999-SAK/dsa-journney))
- Strivioco: matching runners with clubs and events
