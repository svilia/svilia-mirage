from playwright.async_api import async_playwright
import asyncio
from pathlib import Path
from ..core.logger import logger

async def capture_screenshot(url: str, output_path: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        await page.screenshot(path=output_path)
        await browser.close()
        logger.info(f"Screenshot captured for {url}")
        return output_path
