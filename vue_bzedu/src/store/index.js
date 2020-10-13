import Vue from 'vue'

import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        // 购物车数据
        cart_count: 0,
    },
    mutations:{
        change_count(state,data){
            state.cart_count=data;
        },
    }
})
