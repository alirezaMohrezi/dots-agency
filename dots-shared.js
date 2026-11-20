(() => {
  "use strict";
  const form = document.querySelector("#form");

  if (form) {
    const name = form.elements.name;
    const contact = form.elements.contact;
    const company = form.elements.company;
    const message = form.elements.message;
    const status = document.querySelector("#status");
    const options = document.querySelector("#request-options");
    const email = options.querySelector("[data-request-email]");
    const sms = options.querySelector("[data-request-sms]");
    const digits = "۰۱۲۳۴۵۶۷۸۹";
    const normalize = (value) => value.replace(/[۰-۹]/g, (digit) => digits.indexOf(digit))
      .replace(/[٠-٩]/g, (digit) => "٠١٢٣٤٥٦٧٨٩".indexOf(digit));
    const phone = (value) => /^\+?[0-9\s().-]+$/.test(value) && value.replace(/\D/g, "").length >= 10;
    const isMail = (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    const mobile = matchMedia("(max-width: 860px), (pointer: coarse)");
    const showError = (input, message) => {
      document.getElementById(input.id + "-err").textContent = message;
      if (message) input.setAttribute("aria-invalid", "true");
      else input.removeAttribute("aria-invalid");
    };
    const clearDraft = () => {
      if (options.hidden) return;
      options.hidden = true;
      email.removeAttribute("href");
      sms.removeAttribute("href");
      status.textContent = "";
    };

    form.addEventListener("input", (event) => {
      clearDraft();
      if (event.target === name || event.target === contact) showError(event.target, "");
    });

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const nameValue = name.value.trim();
      const contactValue = normalize(contact.value.trim());
      const validContact = isMail(contactValue) || phone(contactValue);
      showError(name, nameValue ? "" : "نام خود را وارد کنید.");
      showError(contact, validContact ? "" : "شمارهٔ تلفن یا نشانی ایمیل معتبر وارد کنید.");
      if (!nameValue || !validContact) {
        (nameValue ? contact : name).focus();
        return;
      }
      const lines = [
        "نام: " + nameValue,
        "راه تماس: " + contactValue,
        company.value.trim() ? "کسب‌وکار: " + company.value.trim() : "",
        message.value.trim() ? "چالش فروش: " + message.value.trim() : ""
      ].filter(Boolean);
      const subject = encodeURIComponent("درخواست گفت‌وگوی اولیه با DOT’s");
      const body = encodeURIComponent(lines.join("\n"));
      email.href = "mailto:alireza.mohrezi1991@gmail.com?subject=" + subject + "&body=" + body;
      sms.hidden = !mobile.matches;
      const separator = /iP(hone|ad|od)/.test(navigator.userAgent) ? "&" : "?";
      if (mobile.matches) sms.href = "sms:+989132289608" + separator + "body=" + body;
      status.textContent = "متن درخواست آماده است. آن را در برنامهٔ ایمیل یا پیامک خود ارسال کنید.";
      if (!mobile.matches) status.textContent = "متن درخواست آماده است. آن را در برنامهٔ ایمیل خود ارسال کنید.";
      options.hidden = false;
      email.focus();
    });
  }

  const filter = document.querySelector(".wfilter");
  const categories = new Set(["growth", "digital", "campaign", "brand"]);
  if (filter) {
    const retainCategory = () => {
      const category = new URL(location.href).searchParams.get("c");
      for (const card of document.querySelectorAll("a.wcard[data-cat]")) {
        const url = new URL(card.href, location.href);
        if (categories.has(category)) url.searchParams.set("from", category);
        else url.searchParams.delete("from");
        card.href = url.pathname.split("/").pop() + url.search;
      }
    };
    filter.addEventListener("click", () => queueMicrotask(retainCategory));
    retainCategory();
  }
  const from = new URL(location.href).searchParams.get("from");
  if (categories.has(from)) {
    for (const back of document.querySelectorAll("[data-portfolio-back]")) {
      back.href = "work.html?c=" + from + "#project-filters";
    }
  }
})();
