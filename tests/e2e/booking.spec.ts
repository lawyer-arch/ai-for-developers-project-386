import { test, expect } from "@playwright/test";

function getWeekday(offsetDays: number): string {
  const date = new Date();
  date.setDate(date.getDate() + offsetDays);
  while (date.getDay() === 0 || date.getDay() === 6) {
    date.setDate(date.getDate() + 1);
  }
  return date.toISOString().split("T")[0];
}

test.describe("Booking flow", () => {
  test("complete booking: homepage → select slot → fill form → confirm", async ({
    page,
  }) => {
    // 1. Открываем главную страницу
    await page.goto("/");

    // 2. Ждём загрузки списка event types
    await expect(page.getByText("Event Types")).toBeVisible();

    // 3. Убеждаемся, что виден "Consultation"
    const consultationCard = page.getByText("Consultation").first();
    await expect(consultationCard).toBeVisible();

    // 4. Нажимаем "View booking page" → переход на страницу бронирования
    await page.getByText("View booking page").first().click();
    await expect(page).toHaveURL(/\/demo\/consult/);

    // 5. Ждём загрузки заголовка event type на странице бронирования
    await expect(page.getByRole("heading", { name: "Consultation" })).toBeVisible();

    // 6. Выбираем будний день (сегодня или следующий будний)
    const weekday = getWeekday(0);
    const dateInput = page.locator('input[type="date"]');
    await dateInput.fill(weekday);

    // 7. Ждём загрузки слотов
    await expect(page.getByText("Available times")).toBeVisible();

    // 8. Кликаем первый доступный слот
    const firstSlot = page.locator("button").filter({ hasText: /^\d{2}:\d{2}$/ }).first();
    await expect(firstSlot).toBeVisible();
    await firstSlot.click();

    // 9. Заполняем форму
    await expect(page.getByText("Enter your details")).toBeVisible();

    await page.getByLabel("Name *").fill("Test User");
    await page.getByLabel("Email *").fill("test@example.com");

    // 10. Нажимаем "Confirm Booking"
    await page.getByRole("button", { name: "Confirm Booking" }).click();

    // 11. Проверяем, что появилось сообщение об успешном бронировании
    await expect(page.getByText("Booked!")).toBeVisible();
    await expect(
      page.getByText("Your meeting has been scheduled")
    ).toBeVisible();
  });

  test("homepage shows event types list", async ({ page }) => {
    await page.goto("/");

    await expect(page.getByText("Event Types")).toBeVisible();
    await expect(page.getByText("Consultation")).toBeVisible();
    await expect(page.getByText("/consult")).toBeVisible();
    await expect(page.getByText("30 min")).toBeVisible();
  });

  test("booking page shows event details", async ({ page }) => {
    await page.goto("/demo/consult");

    await expect(page.getByRole("heading", { name: "Consultation" })).toBeVisible();
    await expect(page.getByText("30 minutes")).toBeVisible();
    await expect(page.getByText("Hosted by demo")).toBeVisible();
  });
});
