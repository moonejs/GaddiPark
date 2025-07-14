from flask import Blueprint,render_template,request,redirect,url_for,session
from routes.decorators import login_required,admin_required
from models import ParkingLot,User,ParkingSpot,Booking,History

admin_bp=Blueprint('admin',__name__)

@admin_bp.route('/admin_dashboard')
@login_required
@admin_required
def admin_dashboard():
    lots=ParkingLot.query.all()
    lot_id=request.args.get('lot_id')
    user = User.query.get(session.get('user_id'))
    spots=ParkingSpot.query.all()
    
    def spots_count(is_ev):
        return ParkingSpot.query.filter_by(is_ev_spot=is_ev).count()
    
    total_regular_available_spots=ParkingSpot.query.filter_by(status='available',is_ev_spot=0).count()
    
    total_ev_available_spots=ParkingSpot.query.filter_by(status='available',is_ev_spot=1).count()
    
    total_regular_spots=spots_count(0)
    total_ev_spots=spots_count(1)
    
    
    active_bookings=Booking.query.count()
    
    total_users=User.query.count() - 1
    lot = None
    if lot_id:
        lot=ParkingLot.query.filter_by(id=lot_id).first()
    history=History.query.all()
    total_revenue=0
    for h in history:
        total_revenue+=h.total_amount_paid
    
    return render_template('admin_dashboard.html',lots=lots,lot=lot,user=user,spots=spots,total_regular_available_spots=total_regular_available_spots,total_users=total_users,total_ev_available_spots=total_ev_available_spots,total_regular_spots=total_regular_spots,total_ev_spots=total_ev_spots,active_bookings=active_bookings,total_revenue=total_revenue)



@admin_bp.route('/users_summery')
@login_required
@admin_required
def users_summery():
    user=User.query.get(session.get('user_id'))
    users= User.query.all()
    history= History.query.all()
    bookings=Booking.query.all()
    spots=ParkingSpot.query.all()
    lots=ParkingLot.query.all()
    return render_template('users_summery.html',users=users,history=history,bookings=bookings,spots=spots,user=user,lots=lots)



@admin_bp.route('/admin/charts')
@login_required
@admin_required
def admin_charts():
    user=User.query.get(session.get('user_id'))
    regular_spots=History.query.filter_by(is_ev_spot=0).count()
    ev_spots=History.query.filter_by(is_ev_spot=1).count()
    history=History.query.all()
    lots_dict={}
    month_dict={}
    for h in history:
        lot=ParkingLot.query.get(h.lot_id)
        lots_dict[lot.name]=lots_dict.get(lot.name,0)+1
        month = h.exit_time.strftime('%m')
        month_dict[month]=month_dict.get(month,0)+h.total_amount_paid
    
    month_names_chart3_labels= ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    revenue=[0]*12
    month_num=list(month_dict.keys())
    
    total_revenue_lst=list(month_dict.values())
    
    for i in range(len(month_num)):
        revenue[int(month_num[i])]=total_revenue_lst[i]
    
    chart3_data=revenue
    
    
    lot_names_chart2_labels=list(lots_dict.keys())
    chart2_data=list(lots_dict.values())
    
    best_lot = lot_names_chart2_labels[chart2_data.index(max(chart2_data))]
    
    peak_month=month_names_chart3_labels[int(month_num[total_revenue_lst.index(max(total_revenue_lst))])-1]
    
    
    chart1_labels=['Regular Vehicles','Ev Vehicles']
    chart1_data=[regular_spots,ev_spots]
    return render_template('admin_charts.html',chart1_labels=chart1_labels,chart1_data=chart1_data,lot_names_chart2_labels=lot_names_chart2_labels,chart2_data=chart2_data,month_names_chart3_labels=month_names_chart3_labels,chart3_data=chart3_data,user=user,best_lot=best_lot,peak_month=peak_month)