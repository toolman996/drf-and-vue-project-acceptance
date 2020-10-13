import Vue from 'vue'
import Router from 'vue-router'
import Index from "../components/Index";
import Login from "../components/Login";
import Register from "../components/Register";
import Course from "../components/Course";
import CourseDetail from "../components/CourseDetail";
import CartItem from "../components/common/CartItem";
import Shoppingcart from "../components/Shoppingcart";
import Order from "../components/Order";
import PaymentSuccess from "../components/PaymentSuccess";

Vue.use(Router)

export default new Router({
    mode:'history',
    routes: [
        {
            path: '/',
            component: Index,
        },
        {
            path: '/index',
            component: Index,
        },
        {
            path: '/home/login',
            component: Login,
        },
        {
            path: '/user/register',
            component: Register,
        },
        {
            path: '/course',
            component: Course,
        },
        {
            path: '/course/:id',
            component: CourseDetail,
        },
        {
            path: '/shoppingcart',
            component: Shoppingcart,
        },
        {
            path: '/cartitem',
            component: CartItem,
        },
        {
            path: '/order',
            component: Order,
        },
        {
            path: '/payoff/result',
            component: PaymentSuccess,
        },
    ]
})
