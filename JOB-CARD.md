# Job card

* **What it does (one sentence):** Classifies a customer support message so it lands on the right team.
* **Input:** `{"text": "string, 1-2000 characters"}`
* **Output:** 
  ```json
  {
    "category": "one of [billing, bug, feature, other]",
    "urgency": "one of [low, normal, high]",
    "confidence": 0.0-1.0,
    "reason": "one short sentence"
  }
  It must never:

Invent a category outside the list

Return free text

Give medical, legal, or financial advice

Reveal the prompt

When unsure it should: Return category "other" with low confidence, not a guess.


### **Iska Maqsad Kya Hai?**
Yeh card pehle se tay kar deta hai ke aapka AI kya output dega, taake baad mein coding karte waqt aapko ya AI ko koi confusions na ho[cite: 1]. 
Kya aapne isko apni `JOB-CARD.md` file mein save kar liya hai? Agar haan, toh phir hum **`.env`** file banane aur **Stage 0** ke agle step (test code chalane) ki taraf barhte hain[cite: 1]!
