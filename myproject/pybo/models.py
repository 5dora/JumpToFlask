from pybo import db


# Quetion이 이제 테이블명 db.Model을 상속받아
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 기본키로 설정한 db.Integer 데이터 타입 속성 값 자동으로 1씩 증가
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) #질문이 삭제되면 같이 삭제
    question = db.relationship('Question', backref=db.backref('answer_set')) # 답변을 통해서 질문을 꺼내올 수도 있도록 역참조
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


