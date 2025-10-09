from fastapi import FastAPI, UploadFile, File
import whisper
import os
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Speech-to-Text API", version="1.0")

# Load Whisper model once during startup (faster performance)
model = whisper.load_model("base")

# Endpoint to check if API is running
@app.get("/")
async def root():
    return {"message": "🎤 Speech-to-Text API is running!"}

# Transcription endpoint
@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        # Save the uploaded audio temporarily
        temp_file = "temp_audio.wav"
        with open(temp_file, "wb") as f:
            f.write(await file.read())

        # Run Whisper transcription
        result = model.transcribe(temp_file)
        text = result["text"]

        # Clean up
        os.remove(temp_file)

        return {"success": True, "transcription": text}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run("src.api_server:app", host="127.0.0.1", port=8000, reload=True)
