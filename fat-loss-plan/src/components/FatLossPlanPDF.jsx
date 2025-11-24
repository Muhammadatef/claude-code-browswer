import React, { useState } from 'react';
import { Download } from 'lucide-react';

const FatLossPlanPDF = () => {
  const [generating, setGenerating] = useState(false);

  const generatePDF = () => {
    setGenerating(true);
    setTimeout(() => {
      const printWindow = window.open('', '_blank');
      printWindow.document.write(`
<!DOCTYPE html>
<html>
<head>
  <title>12-Week Fat Loss Plan - Nov 24, 2025 to Feb 18, 2026</title>
  <style>
    @media print {
      body { margin: 0; }
      .page-break { page-break-before: always; }
    }
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      color: #333;
      max-width: 210mm;
      margin: 0 auto;
      padding: 20px;
    }
    h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
    h2 { color: #34495e; background: #ecf0f1; padding: 10px; margin-top: 25px; }
    h3 { color: #2980b9; margin-top: 20px; }
    .stats-box {
      background: #e8f4f8;
      border-left: 4px solid #3498db;
      padding: 15px;
      margin: 20px 0;
    }
    .meal-card, .workout-card {
      background: #f9f9f9;
      border: 1px solid #ddd;
      padding: 15px;
      margin: 15px 0;
      border-radius: 5px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 15px 0;
    }
    th {
      background: #34495e;
      color: white;
      padding: 12px;
      text-align: left;
    }
    td {
      padding: 10px;
      border-bottom: 1px solid #ddd;
    }
    tr:hover { background: #f5f5f5; }
    .exercise-detail {
      margin-left: 20px;
      color: #555;
      font-size: 0.95em;
    }
    ul { margin: 10px 0; }
    li { margin: 8px 0; }
    .highlight {
      background: #fff3cd;
      padding: 10px;
      border-left: 3px solid #ffc107;
      margin: 15px 0;
    }
    .footer {
      margin-top: 30px;
      padding-top: 20px;
      border-top: 2px solid #ddd;
      text-align: center;
      color: #777;
    }
  </style>
</head>
<body>

<h1>🎯 12-WEEK FAT LOSS TRANSFORMATION PLAN</h1>
<p><strong>Duration:</strong> November 24, 2025 → February 18, 2026</p>
<p><strong>Prepared for:</strong> 29 years old | 93.5 kg | 175 cm | Male</p>

<div class="stats-box">
  <h3>📊 Your Starting Stats & Goals</h3>
  <ul>
    <li><strong>Current Weight:</strong> 93.5 kg</li>
    <li><strong>Current BMI:</strong> 30.5 (Overweight)</li>
    <li><strong>Target Weight:</strong> 81-85 kg</li>
    <li><strong>Expected Fat Loss:</strong> 8-12 kg over 12 weeks</li>
    <li><strong>Weekly Target:</strong> 0.7-1.0 kg per week</li>
    <li><strong>Daily Calories:</strong> 2,000-2,200 calories</li>
    <li><strong>Protein Target:</strong> 180-200g per day</li>
  </ul>
</div>

<div class="page-break"></div>

<h2>🍽️ DAILY MEAL PLAN (Rotating 7-Day Cycle)</h2>

<h3>DAY 1 - Monday (2,100 calories)</h3>

<div class="meal-card">
  <h4>🌅 MEAL 1: Breakfast (7:00 AM) - 450 calories</h4>
  <p><strong>Scrambled Eggs with Whole Wheat Toast & Avocado</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>3 whole eggs</li>
    <li>2 slices whole wheat bread</li>
    <li>1/2 avocado (50g)</li>
    <li>1 cup black coffee or green tea</li>
    <li>Salt, pepper, olive oil spray</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Heat non-stick pan with olive oil spray on medium heat</li>
    <li>Crack eggs into bowl, whisk with salt and pepper</li>
    <li>Pour into pan, gently stir until cooked (3-4 minutes)</li>
    <li>Toast bread until golden</li>
    <li>Slice avocado and place on toast</li>
    <li>Serve eggs alongside toast</li>
  </ol>
  <p><strong>Macros:</strong> 28g protein | 38g carbs | 22g fat</p>
</div>

<div class="meal-card">
  <h4>🥤 MEAL 2: Mid-Morning Snack (10:00 AM) - 200 calories</h4>
  <p><strong>Greek Yogurt with Berries</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>150g plain Greek yogurt (0% fat)</li>
    <li>50g mixed berries (blueberries, strawberries)</li>
    <li>5g honey</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Spoon yogurt into bowl</li>
    <li>Wash and add berries on top</li>
    <li>Drizzle honey over</li>
  </ol>
  <p><strong>Macros:</strong> 18g protein | 22g carbs | 1g fat</p>
</div>

<div class="meal-card">
  <h4>🍗 MEAL 3: Lunch (1:00 PM) - 600 calories</h4>
  <p><strong>Grilled Chicken Breast with Brown Rice & Vegetables</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>200g chicken breast</li>
    <li>100g brown rice (uncooked weight)</li>
    <li>150g mixed vegetables (broccoli, carrots, bell peppers)</li>
    <li>1 tbsp olive oil</li>
    <li>Garlic, lemon, herbs (oregano, thyme)</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Rinse rice, cook in 2 cups water for 25-30 minutes</li>
    <li>Season chicken with salt, pepper, garlic powder, herbs</li>
    <li>Heat 1 tsp olive oil in grill pan on medium-high heat</li>
    <li>Grill chicken 6-7 minutes per side until internal temp 75°C</li>
    <li>Steam or stir-fry vegetables with remaining olive oil</li>
    <li>Squeeze lemon juice over chicken before serving</li>
  </ol>
  <p><strong>Macros:</strong> 52g protein | 55g carbs | 16g fat</p>
</div>

<div class="meal-card">
  <h4>🥜 MEAL 4: Afternoon Snack (4:00 PM) - 250 calories</h4>
  <p><strong>Protein Shake with Banana & Almonds</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>1 scoop whey protein powder (30g)</li>
    <li>1 medium banana</li>
    <li>10 almonds (12g)</li>
    <li>250ml unsweetened almond milk</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Add all ingredients to blender</li>
    <li>Blend for 30-45 seconds until smooth</li>
    <li>Consume 30-60 minutes before workout</li>
  </ol>
  <p><strong>Macros:</strong> 30g protein | 28g carbs | 8g fat</p>
</div>

<div class="meal-card">
  <h4>🐟 MEAL 5: Dinner (7:30 PM) - 600 calories</h4>
  <p><strong>Baked Salmon with Quinoa & Roasted Vegetables</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>180g salmon fillet</li>
    <li>80g quinoa (uncooked)</li>
    <li>200g vegetables (zucchini, asparagus, cherry tomatoes)</li>
    <li>1 tbsp olive oil</li>
    <li>Lemon, dill, garlic</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Preheat oven to 200°C</li>
    <li>Rinse quinoa, cook in 1.5 cups water for 15 minutes</li>
    <li>Place salmon on baking sheet, season with salt, pepper, dill</li>
    <li>Chop vegetables, toss with olive oil, garlic, salt</li>
    <li>Arrange vegetables around salmon</li>
    <li>Bake for 15-18 minutes until salmon flakes easily</li>
    <li>Squeeze lemon over salmon before serving</li>
  </ol>
  <p><strong>Macros:</strong> 42g protein | 48g carbs | 22g fat</p>
</div>

<div class="page-break"></div>

<h3>DAY 2 - Tuesday (2,150 calories)</h3>

<div class="meal-card">
  <h4>🌅 MEAL 1: Breakfast (7:00 AM) - 480 calories</h4>
  <p><strong>Oatmeal with Protein Powder & Nuts</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>60g rolled oats</li>
    <li>1 scoop whey protein (30g)</li>
    <li>15g mixed nuts (almonds, walnuts)</li>
    <li>1 small apple, diced</li>
    <li>Cinnamon</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Cook oats in 300ml water or milk for 5 minutes</li>
    <li>Remove from heat, stir in protein powder</li>
    <li>Add diced apple and nuts on top</li>
    <li>Sprinkle cinnamon</li>
  </ol>
  <p><strong>Macros:</strong> 35g protein | 52g carbs | 14g fat</p>
</div>

<div class="meal-card">
  <h4>🥤 MEAL 2: Mid-Morning Snack (10:00 AM) - 180 calories</h4>
  <p><strong>Boiled Eggs with Cucumber</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>2 large eggs (boiled)</li>
    <li>1 medium cucumber, sliced</li>
    <li>Salt, pepper</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Boil eggs for 10 minutes, cool in cold water</li>
    <li>Peel and slice</li>
    <li>Serve with sliced cucumber</li>
  </ol>
  <p><strong>Macros:</strong> 13g protein | 5g carbs | 10g fat</p>
</div>

<div class="meal-card">
  <h4>🥩 MEAL 3: Lunch (1:00 PM) - 620 calories</h4>
  <p><strong>Lean Beef Stir-Fry with Vegetables & Sweet Potato</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>180g lean beef sirloin, sliced</li>
    <li>200g sweet potato</li>
    <li>150g stir-fry vegetables (bell peppers, onions, snap peas)</li>
    <li>1 tbsp olive oil</li>
    <li>Soy sauce (low sodium), ginger, garlic</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Cube sweet potato, microwave 5-6 minutes or bake at 200°C for 25 minutes</li>
    <li>Heat wok or large pan with olive oil on high heat</li>
    <li>Stir-fry beef 3-4 minutes until browned, remove</li>
    <li>Stir-fry vegetables 3-4 minutes</li>
    <li>Return beef, add soy sauce, ginger, garlic</li>
    <li>Serve over sweet potato</li>
  </ol>
  <p><strong>Macros:</strong> 48g protein | 52g carbs | 20g fat</p>
</div>

<div class="meal-card">
  <h4>🥜 MEAL 4: Afternoon Snack (4:00 PM) - 220 calories</h4>
  <p><strong>Cottage Cheese with Pineapple</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>150g low-fat cottage cheese</li>
    <li>80g fresh pineapple chunks</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Spoon cottage cheese into bowl</li>
    <li>Add pineapple chunks</li>
    <li>Mix gently</li>
  </ol>
  <p><strong>Macros:</strong> 22g protein | 18g carbs | 6g fat</p>
</div>

<div class="meal-card">
  <h4>🍗 MEAL 5: Dinner (7:30 PM) - 650 calories</h4>
  <p><strong>Turkey Meatballs with Whole Wheat Pasta & Marinara</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>200g ground turkey (93% lean)</li>
    <li>80g whole wheat pasta (uncooked)</li>
    <li>150g marinara sauce (no sugar added)</li>
    <li>50g spinach</li>
    <li>1 egg, breadcrumbs, Italian herbs</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Mix ground turkey, egg, 30g breadcrumbs, herbs, salt, pepper</li>
    <li>Form into 8-10 meatballs</li>
    <li>Bake at 190°C for 20 minutes or pan-fry</li>
    <li>Cook pasta according to package (8-10 minutes)</li>
    <li>Heat marinara sauce, add spinach to wilt</li>
    <li>Combine pasta, meatballs, and sauce</li>
  </ol>
  <p><strong>Macros:</strong> 52g protein | 58g carbs | 18g fat</p>
</div>

<div class="page-break"></div>

<h3>DAY 3 - Wednesday (2,080 calories)</h3>

<div class="meal-card">
  <h4>🌅 MEAL 1: Breakfast (7:00 AM) - 420 calories</h4>
  <p><strong>Whole Wheat Pancakes with Protein & Berries</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>50g whole wheat flour</li>
    <li>1 scoop protein powder</li>
    <li>1 egg</li>
    <li>100ml almond milk</li>
    <li>80g mixed berries</li>
    <li>Cooking spray</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Mix flour, protein powder in bowl</li>
    <li>Whisk egg and milk, combine with dry ingredients</li>
    <li>Heat non-stick pan with cooking spray</li>
    <li>Pour batter to make 3-4 pancakes</li>
    <li>Cook 2-3 minutes per side until golden</li>
    <li>Top with berries</li>
  </ol>
  <p><strong>Macros:</strong> 38g protein | 48g carbs | 8g fat</p>
</div>

<div class="meal-card">
  <h4>🥤 MEAL 2: Mid-Morning Snack (10:00 AM) - 160 calories</h4>
  <p><strong>Apple with Peanut Butter</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>1 medium apple</li>
    <li>15g natural peanut butter (1 tbsp)</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Slice apple into wedges</li>
    <li>Serve with peanut butter for dipping</li>
  </ol>
  <p><strong>Macros:</strong> 4g protein | 22g carbs | 8g fat</p>
</div>

<div class="meal-card">
  <h4>🐔 MEAL 3: Lunch (1:00 PM) - 580 calories</h4>
  <p><strong>Chicken Shawarma Bowl with Hummus</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>180g chicken breast, sliced</li>
    <li>100g brown rice</li>
    <li>100g mixed salad (lettuce, tomatoes, cucumber)</li>
    <li>50g hummus</li>
    <li>Shawarma spices (cumin, paprika, turmeric, garlic)</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Cook brown rice</li>
    <li>Marinate chicken in shawarma spices, lemon juice, olive oil (30 min)</li>
    <li>Grill or pan-fry chicken 6-7 minutes per side</li>
    <li>Slice chicken</li>
    <li>Assemble bowl: rice, salad, chicken, hummus</li>
  </ol>
  <p><strong>Macros:</strong> 46g protein | 52g carbs | 16g fat</p>
</div>

<div class="meal-card">
  <h4>🥜 MEAL 4: Afternoon Snack (4:00 PM) - 240 calories</h4>
  <p><strong>Protein Bar & Orange</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>1 protein bar (20g protein)</li>
    <li>1 medium orange</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Consume protein bar</li>
    <li>Peel and eat orange</li>
  </ol>
  <p><strong>Macros:</strong> 22g protein | 32g carbs | 6g fat</p>
</div>

<div class="meal-card">
  <h4>🦐 MEAL 5: Dinner (7:30 PM) - 680 calories</h4>
  <p><strong>Grilled Shrimp with Couscous & Vegetables</strong></p>
  <p><strong>Ingredients:</strong></p>
  <ul>
    <li>250g large shrimp, peeled</li>
    <li>80g whole wheat couscous</li>
    <li>150g vegetables (zucchini, bell peppers)</li>
    <li>1 tbsp olive oil</li>
    <li>Lemon, garlic, parsley</li>
  </ul>
  <p><strong>Preparation:</strong></p>
  <ol>
    <li>Pour boiling water over couscous (1:1 ratio), cover 5 minutes</li>
    <li>Marinate shrimp with garlic, lemon, olive oil (15 min)</li>
    <li>Grill shrimp 2-3 minutes per side</li>
    <li>Sauté vegetables in remaining oil</li>
    <li>Fluff couscous, mix in parsley</li>
    <li>Serve shrimp over couscous with vegetables</li>
  </ol>
  <p><strong>Macros:</strong> 58g protein | 54g carbs | 18g fat</p>
</div>

<div class="page-break"></div>

<h3>DAYS 4-7: Continue Rotation</h3>

<div class="highlight">
  <h4>📋 Quick Reference for Remaining Days:</h4>
  <p><strong>Day 4 (Thursday):</strong> Repeat Day 1 meals or substitute with similar protein/carb/fat ratios</p>
  <p><strong>Day 5 (Friday):</strong> Repeat Day 2 meals</p>
  <p><strong>Day 6 (Saturday):</strong> Repeat Day 3 meals or try new combinations</p>
  <p><strong>Day 7 (Sunday):</strong> REFEED DAY - Add 300-400 extra calories from healthy carbs (sweet potato, rice, fruits)</p>
</div>

<h3>🥘 Alternative Meal Options (Same Macros)</h3>

<div class="meal-card">
  <h4>Breakfast Alternatives:</h4>
  <ul>
    <li>Egg white omelet (6 whites) + 2 whole wheat toast + 1 tbsp almond butter</li>
    <li>Protein smoothie: 2 scoops protein, banana, spinach, oats, almond milk</li>
    <li>Turkey sausage (3 links) + scrambled eggs (2) + fruit</li>
  </ul>
</div>

<div class="meal-card">
  <h4>Lunch Alternatives:</h4>
  <ul>
    <li>Tuna salad (200g tuna) + mixed greens + olive oil dressing + whole grain crackers</li>
    <li>Chicken breast + baked potato + steamed broccoli</li>
    <li>Lamb kofta (150g) + tabbouleh salad + hummus</li>
  </ul>
</div>

<div class="meal-card">
  <h4>Dinner Alternatives:</h4>
  <ul>
    <li>Baked cod + roasted vegetables + quinoa</li>
    <li>Chicken curry (made with light coconut milk) + brown rice</li>
    <li>Beef and vegetable stew + whole grain roll</li>
  </ul>
</div>

<div class="page-break"></div>

<h2>💪 12-WEEK GYM TRAINING PROGRAM</h2>

<div class="highlight">
  <h3>Training Split Overview</h3>
  <p><strong>Schedule:</strong> 5 days weight training + 2-3 days cardio per week</p>
  <p><strong>Duration:</strong> 60-75 minutes per session</p>
  <p><strong>Rest:</strong> 60-90 seconds between sets for compounds, 45-60 seconds for isolation</p>
</div>

<h3>📅 WEEKLY TRAINING SCHEDULE</h3>

<table>
  <tr>
    <th>Day</th>
    <th>Focus</th>
    <th>Cardio</th>
  </tr>
  <tr>
    <td>Monday</td>
    <td>Chest & Triceps</td>
    <td>20 min LISS post-workout</td>
  </tr>
  <tr>
    <td>Tuesday</td>
    <td>Back & Biceps</td>
    <td>20 min LISS post-workout</td>
  </tr>
  <tr>
    <td>Wednesday</td>
    <td>REST or 30 min Cardio</td>
    <td>Optional: 30 min moderate cardio</td>
  </tr>
  <tr>
    <td>Thursday</td>
    <td>Shoulders & Abs</td>
    <td>20 min LISS post-workout</td>
  </tr>
  <tr>
    <td>Friday</td>
    <td>Legs</td>
    <td>15 min LISS post-workout</td>
  </tr>
  <tr>
    <td>Saturday</td>
    <td>Full Body / Arms</td>
    <td>20 min LISS post-workout</td>
  </tr>
  <tr>
    <td>Sunday</td>
    <td>REST</td>
    <td>Active recovery: walking, stretching</td>
  </tr>
</table>

<div class="page-break"></div>

<h3>🏋️ MONDAY: CHEST & TRICEPS</h3>

<div class="workout-card">
  <h4>Warm-up (10 minutes)</h4>
  <ul>
    <li>5 minutes treadmill or bike (light pace)</li>
    <li>Arm circles: 10 forward, 10 backward</li>
    <li>Push-ups: 2 sets of 10 reps</li>
    <li>Band pull-aparts: 2 sets of 15 reps</li>
  </ul>
</div>

<table>
  <tr>
    <th>Exercise</th>
    <th>Sets × Reps</th>
    <th>Rest</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><strong>1. Barbell Bench Press</strong></td>
    <td>4 × 8-10</td>
    <td>90 sec</td>
    <td>Main chest builder</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Lie on flat bench, feet flat on floor, grip bar slightly wider than shoulders<br>
        <strong>Execution:</strong> Lower bar to mid-chest, press back up explosively<br>
        <strong>Cues:</strong> Retract shoulder blades, chest up, full range of motion<br>
        <strong>Weight:</strong> Start with 50-60% of body weight, progress weekly
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>2. Incline Dumbbell Press</strong></td>
    <td>3 × 10-12</td>
    <td>75 sec</td>
    <td>Upper chest focus</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Set bench to 30-45 degree incline, dumbbells at shoulder level<br>
        <strong>Execution:</strong> Press dumbbells up and slightly together at top<br>
        <strong>Cues:</strong> Control descent, don't let elbows flare too wide<br>
        <strong>Weight:</strong> Each dumbbell = 25-30% of body weight
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>3. Cable Chest Fly</strong></td>
    <td>3 × 12-15</td>
    <td>60 sec</td>
    <td>Chest stretch & squeeze</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Set cables to shoulder height, step forward with slight bend<br>
        <strong>Execution:</strong> Bring handles together in arc motion, squeeze at center<br>
        <strong>Cues:</strong> Maintain slight elbow bend throughout, feel chest stretch<br>
        <strong>Machine:</strong> Dual cable station or pec deck as alternative
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>4. Dips (Chest Focus)</strong></td>
    <td>3 × 8-12</td>
    <td>60 sec</td>
    <td>Lower chest emphasis</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Grip parallel bars, lean forward slightly<br>
        <strong>Execution:</strong> Lower until shoulders below elbows, press back up<br>
        <strong>Cues:</strong> Chest forward, legs slightly back, control the movement<br>
        <strong>Progression:</strong> Use assisted dip machine if needed, add weight when doing 12+ reps
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>5. Tricep Rope Pushdown</strong></td>
    <td>3 × 12-15</td>
    <td>45 sec</td>
    <td>Tricep isolation</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Cable machine high pulley with rope attachment<br>
        <strong>Execution:</strong> Push rope down, split ends at bottom, squeeze triceps<br>
        <strong>Cues:</strong> Elbows tucked to sides, only forearms move<br>
        <strong>Weight:</strong> Focus on form and contraction
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>6. Overhead Dumbbell Extension</strong></td>
    <td>3 × 10-12</td>
    <td>45 sec</td>
    <td>Long head tricep</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Stand or sit, hold one dumbbell with both hands overhead<br>
        <strong>Execution:</strong> Lower dumbbell behind head, extend arms back up<br>
        <strong>Cues:</strong> Keep elbows close to head, full stretch at bottom<br>
        <strong>Weight:</strong> Start with 15-20% of body weight
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>7. Close-Grip Bench Press</strong></td>
    <td>3 × 8-10</td>
    <td>60 sec</td>
    <td>Tricep mass builder</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Lie on flat bench, grip bar shoulder-width apart<br>
        <strong>Execution:</strong> Lower bar to lower chest, press up focusing on triceps<br>
        <strong>Cues:</strong> Elbows closer to body than regular bench press<br>
        <strong>Weight:</strong> Use 70-80% of your regular bench press weight
      </div>
    </td>
  </tr>
</table>

<div class="workout-card">
  <h4>Post-Workout Cardio</h4>
  <p><strong>LISS (Low-Intensity Steady State):</strong> 20 minutes</p>
  <ul>
    <li>Treadmill walk at 3.5-4.0 mph with 3-5% incline</li>
    <li>Or stationary bike at moderate pace</li>
    <li>Heart rate: 120-140 bpm (60-70% max HR)</li>
  </ul>
</div>

<div class="page-break"></div>

<h3>🏋️ TUESDAY: BACK & BICEPS</h3>

<div class="workout-card">
  <h4>Warm-up (10 minutes)</h4>
  <ul>
    <li>5 minutes rowing machine or bike (light pace)</li>
    <li>Shoulder dislocations with band: 2 sets of 10</li>
    <li>Dead hangs: 2 sets of 20 seconds</li>
    <li>Band rows: 2 sets of 15 reps</li>
  </ul>
</div>

<table>
  <tr>
    <th>Exercise</th>
    <th>Sets × Reps</th>
    <th>Rest</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><strong>1. Deadlifts</strong></td>
    <td>4 × 6-8</td>
    <td>2 min</td>
    <td>Full back development</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Feet hip-width, bar over mid-foot, hands just outside legs<br>
        <strong>Execution:</strong> Drive through heels, keep bar close to body, stand tall<br>
        <strong>Cues:</strong> Chest up, back flat, hinge at hips<br>
        <strong>Weight:</strong> Start with 60-80% of body weight, build up gradually
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>2. Pull-Ups or Lat Pulldown</strong></td>
    <td>4 × 8-12</td>
    <td>90 sec</td>
    <td>Lat width</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Wide overhand grip, hang with arms fully extended<br>
        <strong>Execution:</strong> Pull chest to bar, squeeze shoulder blades together<br>
        <strong>Cues:</strong> Lead with chest, elbows down and back<br>
        <strong>Progression:</strong> Use assisted pull-up machine or lat pulldown if needed
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>3. Barbell Rows</strong></td>
    <td>4 × 8-10</td>
    <td>75 sec</td>
    <td>Mid-back thickness</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Bend at hips, back flat, knees slightly bent<br>
        <strong>Execution:</strong> Pull bar to lower chest/upper abs, squeeze back<br>
        <strong>Cues:</strong> Don't use momentum, keep core tight<br>
        <strong>Weight:</strong> 50-60% of deadlift weight
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>4. Seated Cable Rows</strong></td>
    <td>3 × 10-12</td>
    <td>60 sec</td>
    <td>Back density</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Sit at cable row station, feet on platform<br>
        <strong>Execution:</strong> Pull handle to lower chest, squeeze shoulder blades<br>
        <strong>Cues:</strong> Chest out, slight lean back at end of pull<br>
        <strong>Grip:</strong> Alternate between wide and narrow grip weekly
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>5. Face Pulls</strong></td>
    <td>3 × 15-20</td>
    <td>45 sec</td>
    <td>Rear delts & upper back</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Cable at upper chest height with rope attachment<br>
        <strong>Execution:</strong> Pull rope to face, separate hands at end<br>
        <strong>Cues:</strong> Elbows high, focus on rear delts<br>
        <strong>Weight:</strong> Light weight, focus on contraction
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>6. Barbell Bicep Curls</strong></td>
    <td>3 × 10-12</td>
    <td>60 sec</td>
    <td>Bicep mass</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Stand with feet shoulder-width, underhand grip on bar<br>
        <strong>Execution:</strong> Curl bar up, squeeze biceps at top, lower with control<br>
        <strong>Cues:</strong> Elbows fixed at sides, no swinging<br>
        <strong>Weight:</strong> 25-30% of body weight
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>7. Hammer Curls</strong></td>
    <td>3 × 10-12</td>
    <td>45 sec</td>
    <td>Brachialis & biceps</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Stand with dumbbells, neutral grip (palms facing each other)<br>
        <strong>Execution:</strong> Curl dumbbells up simultaneously or alternating<br>
        <strong>Cues:</strong> Keep wrists neutral, controlled movement<br>
        <strong>Weight:</strong> Slightly heavier than regular curls
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>8. Cable Bicep Curls</strong></td>
    <td>3 × 12-15</td>
    <td>45 sec</td>
    <td>Bicep peak</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Cable machine low pulley with straight or EZ-bar attachment<br>
        <strong>Execution:</strong> Curl cable up, maintain constant tension<br>
        <strong>Cues:</strong> Squeeze at top, slow negative<br>
        <strong>Benefit:</strong> Constant tension throughout range of motion
      </div>
    </td>
  </tr>
</table>

<div class="workout-card">
  <h4>Post-Workout Cardio</h4>
  <p><strong>LISS:</strong> 20 minutes at 60-70% max heart rate</p>
</div>

<div class="page-break"></div>

<h3>🏋️ THURSDAY: SHOULDERS & ABS</h3>

<div class="workout-card">
  <h4>Warm-up (10 minutes)</h4>
  <ul>
    <li>5 minutes light cardio</li>
    <li>Shoulder circles: 2 sets of 10 each direction</li>
    <li>Band shoulder external rotations: 2 sets of 15</li>
    <li>Light dumbbell lateral raises: 2 sets of 12</li>
  </ul>
</div>

<table>
  <tr>
    <th>Exercise</th>
    <th>Sets × Reps</th>
    <th>Rest</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><strong>1. Overhead Press (Barbell or Dumbbell)</strong></td>
    <td>4 × 8-10</td>
    <td>90 sec</td>
    <td>Overall shoulder mass</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Stand or sit, bar at shoulder height<br>
        <strong>Execution:</strong> Press bar overhead, lock out at top<br>
        <strong>Cues:</strong> Core tight, don't lean back excessively<br>
        <strong>Weight:</strong> 40-50% of body weight for barbell
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>2. Lateral Raises</strong></td>
    <td>4 × 12-15</td>
    <td>60 sec</td>
    <td>Side delts (shoulder width)</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Stand with dumbbells at sides, slight bend in elbows<br>
        <strong>Execution:</strong> Raise dumbbells to sides until parallel with floor<br>
        <strong>Cues:</strong> Lead with elbows, slight forward tilt, controlled descent<br>
        <strong>Weight:</strong> Light weight (8-12% of body weight per dumbbell)
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>3. Front Raises</strong></td>
    <td>3 × 10-12</td>
    <td>60 sec</td>
    <td>Front delts</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Stand with dumbbells in front of thighs<br>
        <strong>Execution:</strong> Raise dumbbells forward to shoulder height<br>
        <strong>Cues:</strong> Slight bend in elbows, no swinging<br>
        <strong>Alternative:</strong> Use plate or barbell for variety
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>4. Reverse Pec Deck or Bent-Over Lateral Raises</strong></td>
    <td>3 × 12-15</td>
    <td>60 sec</td>
    <td>Rear delts</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Bend at hips 90°, dumbbells hanging<br>
        <strong>Execution:</strong> Raise dumbbells to sides, squeeze shoulder blades<br>
        <strong>Cues:</strong> Maintain flat back, don't use momentum<br>
        <strong>Machine:</strong> Reverse pec deck is easier to control form
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>5. Arnold Press</strong></td>
    <td>3 × 10-12</td>
    <td>60 sec</td>
    <td>All three delt heads</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Sit with dumbbells at shoulder height, palms facing you<br>
        <strong>Execution:</strong> Press up while rotating palms outward<br>
        <strong>Cues:</strong> Smooth rotation, full range of motion<br>
        <strong>Weight:</strong> Lighter than regular overhead press
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>6. Hanging Leg Raises</strong></td>
    <td>3 × 12-15</td>
    <td>45 sec</td>
    <td>Lower abs</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Hang from pull-up bar<br>
        <strong>Execution:</strong> Raise legs to 90°, lower with control<br>
        <strong>Cues:</strong> Don't swing, tilt pelvis up<br>
        <strong>Regression:</strong> Knee raises if straight legs too difficult
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>7. Cable Crunches</strong></td>
    <td>3 × 15-20</td>
    <td>45 sec</td>
    <td>Upper abs</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Kneel facing cable machine, rope above head<br>
        <strong>Execution:</strong> Crunch down, bringing elbows to knees<br>
        <strong>Cues:</strong> Focus on abs, not pulling with arms<br>
        <strong>Weight:</strong> Moderate, focus on contraction
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>8. Plank</strong></td>
    <td>3 × 45-60 sec</td>
    <td>30 sec</td>
    <td>Core stability</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Forearms on ground, body in straight line<br>
        <strong>Execution:</strong> Hold position, engage entire core<br>
        <strong>Cues:</strong> Don't let hips sag or pike up<br>
        <strong>Progression:</strong> Add weight on back when 60 seconds is easy
      </div>
    </td>
  </tr>
</table>

<div class="workout-card">
  <h4>Post-Workout Cardio</h4>
  <p><strong>LISS:</strong> 20 minutes</p>
</div>

<div class="page-break"></div>

<h3>🏋️ FRIDAY: LEGS</h3>

<div class="workout-card">
  <h4>Warm-up (10 minutes)</h4>
  <ul>
    <li>5 minutes bike or treadmill</li>
    <li>Bodyweight squats: 2 sets of 15</li>
    <li>Leg swings: 10 forward/back, 10 side-to-side each leg</li>
    <li>Hip circles: 10 each direction</li>
  </ul>
</div>

<table>
  <tr>
    <th>Exercise</th>
    <th>Sets × Reps</th>
    <th>Rest</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><strong>1. Barbell Back Squats</strong></td>
    <td>4 × 8-10</td>
    <td>2 min</td>
    <td>Quad & glute mass</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Bar on upper back, feet shoulder-width<br>
        <strong>Execution:</strong> Squat down until thighs parallel, drive up through heels<br>
        <strong>Cues:</strong> Chest up, knees track over toes, full depth<br>
        <strong>Weight:</strong> Start with 60-80% of body weight
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>2. Romanian Deadlifts</strong></td>
    <td>3 × 10-12</td>
    <td>90 sec</td>
    <td>Hamstrings & glutes</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Stand with barbell, slight knee bend<br>
        <strong>Execution:</strong> Hinge at hips, lower bar along legs, feel hamstring stretch<br>
        <strong>Cues:</strong> Keep back flat, push hips back<br>
        <strong>Weight:</strong> 50-60% of deadlift weight
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>3. Leg Press</strong></td>
    <td>3 × 12-15</td>
    <td>75 sec</td>
    <td>Overall leg development</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Sit in leg press machine, feet shoulder-width on platform<br>
        <strong>Execution:</strong> Lower weight until knees at 90°, press back up<br>
        <strong>Cues:</strong> Full range of motion, don't lock knees at top<br>
        <strong>Weight:</strong> 1.5-2x body weight
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>4. Walking Lunges</strong></td>
    <td>3 × 12 each leg</td>
    <td>60 sec</td>
    <td>Quads, glutes, balance</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Hold dumbbells at sides or use bodyweight<br>
        <strong>Execution:</strong> Step forward into lunge, alternate legs<br>
        <strong>Cues:</strong> Keep torso upright, knee doesn't go past toes<br>
        <strong>Weight:</strong> 15-20% body weight per dumbbell
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>5. Leg Curls</strong></td>
    <td>3 × 12-15</td>
    <td>60 sec</td>
    <td>Hamstring isolation</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Lie face down on leg curl machine<br>
        <strong>Execution:</strong> Curl legs up, squeeze hamstrings at top<br>
        <strong>Cues:</strong> Don't lift hips, controlled movement<br>
        <strong>Machine:</strong> Lying or seated leg curl
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>6. Leg Extensions</strong></td>
    <td>3 × 12-15</td>
    <td>60 sec</td>
    <td>Quad isolation</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Sit in leg extension machine<br>
        <strong>Execution:</strong> Extend legs fully, squeeze quads<br>
        <strong>Cues:</strong> Slow descent, pause at top<br>
        <strong>Note:</strong> Don't use excessive weight
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>7. Calf Raises (Standing)</strong></td>
    <td>4 × 15-20</td>
    <td>45 sec</td>
    <td>Calf development</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Stand on calf raise machine or platform<br>
        <strong>Execution:</strong> Raise up on toes, full contraction, lower below platform<br>
        <strong>Cues:</strong> Full range of motion, hold at top<br>
        <strong>Weight:</strong> 100%+ of body weight
      </div>
    </td>
  </tr>
</table>

<div class="workout-card">
  <h4>Post-Workout Cardio</h4>
  <p><strong>LISS:</strong> 15 minutes (legs are taxing, shorter cardio)</p>
</div>

<div class="page-break"></div>

<h3>🏋️ SATURDAY: FULL BODY / ARMS</h3>

<div class="workout-card">
  <h4>Warm-up (8-10 minutes)</h4>
  <ul>
    <li>5 minutes light cardio</li>
    <li>Dynamic stretches</li>
    <li>Resistance band exercises</li>
  </ul>
</div>

<table>
  <tr>
    <th>Exercise</th>
    <th>Sets × Reps</th>
    <th>Rest</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td><strong>1. Incline Barbell Bench Press</strong></td>
    <td>3 × 10-12</td>
    <td>75 sec</td>
    <td>Upper chest</td>
  </tr>

  <tr>
    <td><strong>2. T-Bar Rows or Chest-Supported Rows</strong></td>
    <td>3 × 10-12</td>
    <td>75 sec</td>
    <td>Back thickness</td>
  </tr>

  <tr>
    <td><strong>3. Dumbbell Shoulder Press</strong></td>
    <td>3 × 10-12</td>
    <td>60 sec</td>
    <td>Shoulders</td>
  </tr>

  <tr>
    <td><strong>4. Bulgarian Split Squats</strong></td>
    <td>3 × 10 each leg</td>
    <td>60 sec</td>
    <td>Legs & glutes</td>
  </tr>

  <tr>
    <td><strong>5. Preacher Curls</strong></td>
    <td>3 × 12-15</td>
    <td>45 sec</td>
    <td>Bicep peak</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Sit at preacher bench, arms over pad<br>
        <strong>Execution:</strong> Curl weight up, full contraction<br>
        <strong>Cues:</strong> No shoulder movement, isolated biceps<br>
        <strong>Weight:</strong> Moderate, focus on form
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>6. Skull Crushers (Lying Tricep Extension)</strong></td>
    <td>3 × 12-15</td>
    <td>45 sec</td>
    <td>Triceps</td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="exercise-detail">
        <strong>Setup:</strong> Lie on bench, hold EZ-bar above chest<br>
        <strong>Execution:</strong> Lower bar to forehead, extend back up<br>
        <strong>Cues:</strong> Keep elbows stationary<br>
        <strong>Weight:</strong> 20-25% of body weight
      </div>
    </td>
  </tr>

  <tr>
    <td><strong>7. Concentration Curls</strong></td>
    <td>3 × 12-15</td>
    <td>45 sec</td>
    <td>Bicep isolation</td>
  </tr>

  <tr>
    <td><strong>8. Tricep Dips (Between Benches)</strong></td>
    <td>3 × 12-15</td>
    <td>45 sec</td>
    <td>Tricep endurance</td>
  </tr>
</table>

<div class="workout-card">
  <h4>Post-Workout Cardio</h4>
  <p><strong>LISS:</strong> 20 minutes</p>
</div>

<div class="page-break"></div>

<h2>🎯 PROGRAM PROGRESSION</h2>

<div class="highlight">
  <h3>Progressive Overload Strategy</h3>
  <p><strong>Weekly Progression:</strong></p>
  <ul>
    <li>Increase weight by 2-5% when you can complete all sets with good form</li>
    <li>If you hit the top end of rep range for all sets, increase weight next session</li>
    <li>Track all workouts in a notebook or app</li>
  </ul>
</div>

<h3>📈 12-Week Phase Breakdown</h3>

<table>
  <tr>
    <th>Weeks</th>
    <th>Focus</th>
    <th>Cardio</th>
    <th>Notes</th>
  </tr>
  <tr>
    <td>1-4</td>
    <td>Foundation & Form</td>
    <td>20 min LISS 5x/week</td>
    <td>Master technique, establish baseline</td>
  </tr>
  <tr>
    <td>5-8</td>
    <td>Intensity Increase</td>
    <td>25 min LISS 5x/week + 1 HIIT session</td>
    <td>Increase weights, add HIIT on Wednesday</td>
  </tr>
  <tr>
    <td>9-12</td>
    <td>Peak Fat Loss</td>
    <td>30 min LISS 5x/week + 2 HIIT sessions</td>
    <td>Maximum intensity, finish strong</td>
  </tr>
</table>

<h3>🔥 HIIT Cardio Protocol (Weeks 5+)</h3>

<div class="workout-card">
  <h4>Wednesday HIIT Session (20-25 minutes)</h4>
  <p><strong>Format:</strong> 30 seconds high intensity / 60 seconds low intensity</p>
  <p><strong>Options:</strong></p>
  <ul>
    <li><strong>Treadmill:</strong> Sprint at 10-12 mph / Walk at 3-4 mph</li>
    <li><strong>Bike:</strong> All-out pedaling / Light pedaling</li>
    <li><strong>Rowing:</strong> Max effort / Recovery pace</li>
  </ul>
  <p><strong>Structure:</strong></p>
  <ol>
    <li>5-minute warm-up</li>
    <li>10-15 intervals (30 sec high / 60 sec low)</li>
    <li>5-minute cool-down</li>
  </ol>
</div>

<div class="page-break"></div>

<h2>📋 TRACKING & ACCOUNTABILITY</h2>

<h3>Weekly Check-In Checklist</h3>

<table>
  <tr>
    <th>Day</th>
    <th>Metrics to Track</th>
  </tr>
  <tr>
    <td>Sunday Morning</td>
    <td>
      • Weigh yourself (same time, fasted)<br>
      • Take progress photos (front, side, back)<br>
      • Measure waist, chest, arms, thighs<br>
      • Assess energy levels (1-10)<br>
      • Plan next week's meals
    </td>
  </tr>
  <tr>
    <td>Daily</td>
    <td>
      • Log all meals and calories<br>
      • Track water intake (3-4 liters/day)<br>
      • Record workout performance<br>
      • Sleep quality and hours
    </td>
  </tr>
</table>

<h3>🎯 Milestones & Adjustments</h3>

<div class="meal-card">
  <h4>Every 4 Weeks - Reassess and Adjust:</h4>
  <ul>
    <li><strong>Week 4:</strong> If losing < 0.5 kg/week → reduce calories by 100-150</li>
    <li><strong>Week 4:</strong> If losing > 1.2 kg/week → increase calories by 100-150</li>
    <li><strong>Week 8:</strong> Repeat assessment, adjust calories as needed</li>
    <li><strong>Week 12:</strong> Final assessment, set new goals or transition to maintenance</li>
  </ul>
</div>

<h3>💧 Hydration & Supplements</h3>

<div class="stats-box">
  <h4>Daily Essentials:</h4>
  <ul>
    <li><strong>Water:</strong> 3-4 liters per day (more on training days)</li>
    <li><strong>Electrolytes:</strong> Especially if sweating heavily</li>
    <li><strong>Optional Supplements:</strong>
      <ul>
        <li>Whey protein (for convenience)</li>
        <li>Creatine monohydrate (5g daily)</li>
        <li>Omega-3 (2-3g daily)</li>
        <li>Vitamin D (2000-4000 IU)</li>
        <li>Multivitamin</li>
      </ul>
    </li>
  </ul>
</div>

<div class="page-break"></div>

<h2>⚠️ IMPORTANT GUIDELINES</h2>

<div class="highlight">
  <h3>Safety & Recovery</h3>
  <ul>
    <li><strong>Sleep:</strong> Aim for 7-9 hours per night</li>
    <li><strong>Rest Days:</strong> Take them seriously - recovery is when you grow</li>
    <li><strong>Stretching:</strong> 10-15 minutes daily, especially after workouts</li>
    <li><strong>Listen to Your Body:</strong> If experiencing pain (not soreness), rest or seek advice</li>
    <li><strong>Deload Week:</strong> Consider a deload in week 6 (reduce weight by 30-40% if feeling burnt out)</li>
  </ul>
</div>

<h3>🍕 Cheat Meals & Social Events</h3>

<div class="meal-card">
  <h4>Strategic Approach:</h4>
  <ul>
    <li>One cheat meal per week (Sunday refeed day)</li>
    <li>Don't binge - eat until satisfied, not stuffed</li>
    <li>Choose high-carb options on refeed day</li>
    <li>Get back on plan the next meal - no guilt or extended "cheat days"</li>
    <li>For social events: eat protein-heavy, limit alcohol, skip dessert or bread</li>
  </ul>
</div>

<h3>🎯 Expected Results Timeline</h3>

<table>
  <tr>
    <th>Week</th>
    <th>Expected Progress</th>
  </tr>
  <tr>
    <td>Week 1-2</td>
    <td>Initial water weight loss (1-2 kg), learning routine</td>
  </tr>
  <tr>
    <td>Week 3-4</td>
    <td>Clothes fitting better, more energy, 2-4 kg total loss</td>
  </tr>
  <tr>
    <td>Week 5-8</td>
    <td>Visible muscle definition, 5-8 kg total loss, strength gains</td>
  </tr>
  <tr>
    <td>Week 9-12</td>
    <td>Significant transformation, 8-12 kg total loss, new physique</td>
  </tr>
</table>

<div class="page-break"></div>

<h2>✅ FINAL REMINDERS</h2>

<div class="stats-box">
  <h3>Keys to Success:</h3>
  <ol>
    <li><strong>Consistency > Perfection:</strong> Missing one meal or workout won't ruin progress</li>
    <li><strong>Track Everything:</strong> You can't improve what you don't measure</li>
    <li><strong>Progressive Overload:</strong> Always try to do slightly better than last week</li>
    <li><strong>Protein Priority:</strong> Hit your 180-200g protein target daily</li>
    <li><strong>Patience:</strong> Sustainable fat loss takes time - trust the process</li>
    <li><strong>Enjoy the Journey:</strong> Find meals and workouts you actually like</li>
  </ol>
</div>

<div class="highlight">
  <h3>🚫 Common Mistakes to Avoid:</h3>
  <ul>
    <li>Cutting calories too drastically (stay at 2,000-2,200)</li>
    <li>Doing too much cardio and neglecting weights</li>
    <li>Not eating enough protein</li>
    <li>Skipping rest days</li>
    <li>Comparing yourself to others - focus on YOUR progress</li>
    <li>Giving up after one bad day - get right back on track</li>
  </ul>
</div>

<div class="footer">
  <h3>🎯 YOUR 12-WEEK COMMITMENT</h3>
  <p><strong>Start Date:</strong> November 24, 2025</p>
  <p><strong>End Date:</strong> February 18, 2026</p>
  <p><strong>Goal:</strong> 81-85 kg (8-12 kg fat loss)</p>
  <br>
  <p><em>"Success is the sum of small efforts repeated day in and day out."</em></p>
  <br>
  <p><strong>You've got this! 💪</strong></p>
  <br>
  <p style="font-size: 0.9em; color: #999;">This plan is designed as a comprehensive guide. Consult with healthcare professionals before starting any new diet or exercise program, especially if you have pre-existing health conditions.</p>
</div>

</body>
</html>
      `);
      printWindow.document.close();

      // Wait a bit for the content to load, then trigger print
      setTimeout(() => {
        printWindow.print();
        setGenerating(false);
      }, 250);
    }, 100);
  };

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="bg-white rounded-lg shadow-lg p-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">
          12-Week Fat Loss Transformation Plan
        </h1>

        <div className="bg-blue-50 border-l-4 border-blue-500 p-4 mb-6">
          <h2 className="text-xl font-semibold text-blue-900 mb-2">Your Details</h2>
          <ul className="text-blue-800 space-y-1">
            <li>• Age: 29 years</li>
            <li>• Current Weight: 93.5 kg</li>
            <li>• Height: 175 cm</li>
            <li>• Target: Lose 8-12 kg in 12 weeks</li>
            <li>• Duration: Nov 24, 2025 → Feb 18, 2026</li>
          </ul>
        </div>

        <div className="mb-6">
          <h3 className="text-lg font-semibold text-gray-700 mb-3">What's Included:</h3>
          <ul className="space-y-2 text-gray-600">
            <li className="flex items-start">
              <span className="text-green-500 mr-2">✓</span>
              <span>Complete 7-day meal plan with detailed recipes and macros</span>
            </li>
            <li className="flex items-start">
              <span className="text-green-500 mr-2">✓</span>
              <span>5-day gym training program (Chest, Back, Shoulders, Legs, Full Body)</span>
            </li>
            <li className="flex items-start">
              <span className="text-green-500 mr-2">✓</span>
              <span>Cardio guidelines and HIIT protocols</span>
            </li>
            <li className="flex items-start">
              <span className="text-green-500 mr-2">✓</span>
              <span>Progressive overload strategy for 12 weeks</span>
            </li>
            <li className="flex items-start">
              <span className="text-green-500 mr-2">✓</span>
              <span>Tracking tools and weekly check-in guidelines</span>
            </li>
            <li className="flex items-start">
              <span className="text-green-500 mr-2">✓</span>
              <span>Supplement recommendations and hydration guidelines</span>
            </li>
          </ul>
        </div>

        <button
          onClick={generatePDF}
          disabled={generating}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg flex items-center justify-center space-x-2 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          {generating ? (
            <>
              <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>Generating PDF...</span>
            </>
          ) : (
            <>
              <Download className="w-5 h-5" />
              <span>Download Complete 12-Week Plan (PDF)</span>
            </>
          )}
        </button>

        <p className="mt-4 text-sm text-gray-500 text-center">
          Click the button above to generate and download your personalized plan as a PDF.
          You can then save or print it for easy reference.
        </p>
      </div>
    </div>
  );
};

export default FatLossPlanPDF;
