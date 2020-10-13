<template>
    <div class="cart">
        <Header></Header>
        <div class="cart_info">
            <div class="cart_title">
                <span class="text">我的购物车</span>
                <span class="total">共4门课程</span>
            </div>
            <div class="cart_table">
                <div class="cart_head_row">
                    <span class="doing_row"></span>
                    <span class="course_row">课程</span>
                    <span class="expire_row">有效期</span>
                    <span class="price_row">单价</span>
                    <span class="do_more">操作</span>
                </div>
                <div class="cart_course_list">
                    <CartItem v-for="(value,index) in data" :key="index" :value="value" @del="del_cart(index)"@change_status="count_shoppingcart_total">

                    </CartItem>
                </div>
                <div class="cart_footer_row">
                    <span class="cart_select"><label> <el-checkbox
                        ></el-checkbox><span>全选</span></label></span>
                    <span class="cart_delete"><i class="el-icon-delete"></i> <span>删除</span></span>
                    <router-link class="goto_pay" to="/order">去结算</router-link>
                    <span class="cart_total">总计：¥{{shoppingcart_total}}</span>
                </div>
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>
    import CartItem from './common/CartItem'
    import Header from "./common/Header";
    import Footer from "./common/Footer";
    export default {
        name: "Shoppingcart",
        data(){
            return{
                data:[],
                //购物车总价格
                shoppingcart_total:0.00
            }
        },
        methods:{
            //计算购物车勾选状态下的总价格
            count_shoppingcart_total(){
                let total = 0
                //首先拿到购物车中所有商品
                this.data.forEach((value,index)=>{
                    //判断是否勾选选中则计算没有则不计算
                    if (value.selected){
                        total+=parseInt(value.true_price)
                    }
                    this.shoppingcart_total=total
                })

            },
            //点击购物车判断用户是否登录
            ckeck_user_login(){
                let token=localStorage.user_token || sessionStorage.user_token
                if (!token){
                    let self =this
                    this.$confirm('请先登录，没有登录不能添加购物车',{
                        callback(){
                            self.$router.push('/home/login')
                        }
                    })
                    return false
                }
                return token
            },
            //获取购物车
            get_shoppingcart(){
                let token = this.ckeck_user_login()
                this.$axios.get(`${this.$settings.HOST}shoppingcart/option/`,{
                    headers:{
                        //请求头中声明token
                            'Authorization': 'jwt '+token
                    }
                }).then(success=>{
                    this.data=success.data
                    this.$store.commit('change_count',this.data.length)
                    //在购物车获取成功后计算总价格
                    this.count_shoppingcart_total()
                }).catch(error=>{
                    console.log(error.success);
                })
            },
            //删除购物车
            del_cart(index){
                this.data.splice(index,1)
                //更新购物车数量
                this.$store.commit('change_count',this.data.length)
                this.count_shoppingcart_total()
            },
        },
        components:{
            CartItem,Header,Footer
        },
        created() {
            this.get_shoppingcart()
        }
    }
</script>

<style scoped>
    .cart_info {
        width: 1200px;
        margin: 0 auto 200px;
    }

    .cart_title {
        margin: 25px 0;
    }

    .cart_title .text {
        font-size: 18px;
        color: #666;
    }

    .cart_title .total {
        font-size: 12px;
        color: #d0d0d0;
    }

    .cart_table {
        width: 1170px;
    }

    .cart_table .cart_head_row {
        background: #F7F7F7;
        width: 100%;
        height: 80px;
        line-height: 80px;
        padding-right: 30px;
    }

    .cart_table .cart_head_row::after {
        content: "";
        display: block;
        clear: both;
    }

    .cart_table .cart_head_row .doing_row,
    .cart_table .cart_head_row .course_row,
    .cart_table .cart_head_row .expire_row,
    .cart_table .cart_head_row .price_row,
    .cart_table .cart_head_row .do_more {
        padding-left: 10px;
        height: 80px;
        float: left;
    }

    .cart_table .cart_head_row .doing_row {
        width: 78px;
    }

    .cart_table .cart_head_row .course_row {
        width: 530px;
    }

    .cart_table .cart_head_row .expire_row {
        width: 188px;
    }

    .cart_table .cart_head_row .price_row {
        width: 162px;
    }

    .cart_table .cart_head_row .do_more {
        width: 162px;
    }

    .cart_footer_row {
        padding-left: 30px;
        background: #F7F7F7;
        width: 100%;
        height: 80px;
        line-height: 80px;
    }

    .cart_footer_row .cart_select span {
        margin-left: -7px;
        font-size: 18px;
        color: #666;
    }

    .cart_footer_row .cart_delete {
        margin-left: 58px;
    }

    .cart_delete .el-icon-delete {
        font-size: 18px;
    }

    .cart_delete span {
        margin-left: 15px;
        cursor: pointer;
        font-size: 18px;
        color: #666;
    }

    .cart_total {
        float: right;
        margin-right: 62px;
        font-size: 18px;
        color: #666;
    }

    .goto_pay {
        float: right;
        width: 159px;
        height: 80px;
        outline: none;
        border: none;
        background: #ffc210;
        font-size: 18px;
        color: #fff;
        text-align: center;
        cursor: pointer;
    }
</style>
