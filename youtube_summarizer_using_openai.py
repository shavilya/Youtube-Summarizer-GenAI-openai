from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled,NoTranscriptFound 
import os 
import openai 
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def get_transcript(video_id) : 
    
    try : 
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Prefer English Transcripts 
        transcript = transcript_list.find_transcript(['en'])
        transcript_data = transcript.fetch()
        
        # Combine all transcript parts into single string 
        transcript_text = "".join(item['text'] for item in transcript_data)
        return transcript_text 
    
    except TranscriptsDisabled : 
        print("Transcript are disabled for this video")     
    except NoTranscriptFound : 
        print("No Transcript found for this video")  
    except Exception as e : 
        print(f"An error occured: {e}")
        

def summarize_text(text,max_tokens = 150) : 
    try : 
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {'role':'system','content':'You are an helpful assistant that summarizes text.'},
                {'role':'user','content':f'please provide a concise summary of the following text:\n\n{text}'}
            ],
            max_tokens = max_tokens , 
            n = 1 , 
            stop = None , 
            temperature = 0.5
        )
        summary = response.choices[0].message['content'].strip()
        return summary 
    
    except Exception as e : 
        print(f'An error occured during summarization: {e}')
        return None 
    
def main() : 
    video_url = input("Enter Youtube video URL: ")
    try : 
        video_id = video_url.split("v=")[-1].split("&")[0]
    except IndexError : 
        print("Invalid Youtube URL.")
        
    
    transcript = get_transcript(video_id)
    if transcript : 
        print("\nTranscript fetched successfully.Summarizing....\n")
        summary = summarize_text(transcript)
        if summary: 
            print(f"Summary: {summary}")
            

if __name__ == "__main__" : 
    main()