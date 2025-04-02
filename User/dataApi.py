# dataApi.py
from typing import Optional
from User.dataBaseConfig.dataBaseMgr import db
from User.stateModel import StateModel

def get_current_state(user_id: str) -> Optional[StateModel]:
    try:
        user_doc = db.collection('Users').document(user_id).get()
        if user_doc.exists:
            data = user_doc.to_dict().get('currentState', None)
            if data:
                return StateModel.from_dict(data)
            else:
                return None
        else:
            print(f"No document found for user_id: {user_id}")
            return None
    except Exception as e:
        print(f"Error retrieving current state for user {user_id}: {e}")
        return None

def get_question_state(user_id: str, question_id: str) -> Optional[StateModel]:
    try:
        session_doc = db.collection('Users').document(user_id).collection('sessions').document(question_id).get()
        if session_doc.exists:
            data = session_doc.to_dict()
            return StateModel.from_dict(data)
        else:
            print(f"No session found for question_id: {question_id} for user_id: {user_id}")
            return None
    except Exception as e:
        print(f"Error retrieving question state for question_id {question_id} for user {user_id}: {e}")
        return None

def update_question(user_id: str, question_id: str, question_data: StateModel) -> bool:
    try:
        state_dict = question_data.to_dict()  # 转换为字典
        
        session_ref = db.collection('Users').document(user_id).collection('sessions').document(question_id)
        session_ref.set(state_dict, merge=True)
        
        user_ref = db.collection('Users').document(user_id)
        user_ref.set({'currentState': state_dict}, merge=True)
        return True
    except Exception as e:
        print(f"Error updating question {question_id} for user {user_id}: {e}")
        return False
