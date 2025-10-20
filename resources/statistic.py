from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields
from storage import load_sessions
from collections import defaultdict

blp = Blueprint("Statistics", "statistics", description="Fishing statistics")

# --- schemas ---
class SpeciesBreakdownSchema(Schema):
    species = fields.Dict(keys=fields.Str(), values=fields.Int())

class StatisticsResponseSchema(Schema):
    total_fish_caught = fields.Int(required=True)
    total_weight_kg = fields.Float(required=True)
    species_breakdown = fields.Dict(keys=fields.Str(), values=fields.Int(), required=True)

# --- Resource ---

@blp.route("/statistics")
class StatisticsResource(MethodView):
    @blp.response(200, StatisticsResponseSchema)
    def get(self):
        try:
            sessions = load_sessions()

            total_fish = 0
            total_weight = 0.0
            species_count = defaultdict(int)

            for session in sessions:
                for catch in session.get("catches", []):
                    total_fish += 1
                    total_weight += catch.get("weight_kg", 0.0)
                    species = catch.get("species")
                    if species:
                        species_count[species] += 1

            return {
                "total_fish_caught": total_fish,
                "total_weight_kg": round(total_weight, 2),
                "species_breakdown": dict(species_count)
            }

        except Exception as e:
            abort(500, message=f"Failed to calculate statistics: {str(e)}")
