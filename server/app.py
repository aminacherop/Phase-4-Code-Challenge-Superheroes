from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import Hero, Power, HeroPower
from sqlalchemy.exc import IntegrityError
from extensions import db,migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    return jsonify([hero.to_dict() for hero in Hero.query.all()]), 200

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict(rules=('hero_powers', 'hero_powers.power'))), 200

@app.route('/powers', methods=['GET'])
def get_powers():
    return jsonify([power.to_dict() for power in Power.query.all()]), 200




@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def power_detail(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    if request.method == 'GET':
        return jsonify(power.to_dict()), 200

    if request.method == 'PATCH':
        data = request.get_json()
        try:
            power.description = data['description']
            db.session.commit()
            return jsonify(power.to_dict()), 200
        except Exception:
            return jsonify({"errors": ["validation errors"]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()

        return jsonify({
            "id": hero_power.id,
            "hero_id": hero_power.hero_id,
            "power_id": hero_power.power_id,
            "strength": hero_power.strength,
            "hero": hero_power.hero.to_dict(),
            "power": hero_power.power.to_dict(),
        }), 201
    except Exception:
        return jsonify({"errors": ["validation errors"]}), 400
    
if __name__ == '__main__':
    app.run(debug=True)