from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/vapi-webhook")
async def vapi_webhook(request: Request):
    payload = await request.json()

    """
    Vapi sends a large payload.
    We only care about the final structured output produced by the assistant.
    """
    final_output = payload.get("analysis", {}).get("output")

    if not final_output:
        return {"status": "no final output found"}

    # Save final JSON output
    with open("output.json", "w") as f:
        json.dump(final_output, f, indent=2)

    return {"status": "success", "message": "Lead qualification saved"}