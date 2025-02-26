from flask import Flask, request, jsonify
# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Float32MultiArray

app = Flask(__name__)

# Initialize ROS2 node
# rclpy.init()
# ros_node = Node('ar_coordinates_publisher')
# publisher = ros_node.create_publisher(Float32MultiArray, 'ar_coordinates', 10)

@app.route('/coordinates', methods=['POST'])
def receive_coordinates():
    data = request.json
    if not data:
        return jsonify({'error': 'No data received'}), 400

    # Convert ARKit coordinates to CoppeliaSim's format if needed
    description, x, y, z = data["description"], data['x'], data['y'], data['z']
    coppelia_x, coppelia_y, coppelia_z = convert_to_coppeliasim(x, y, z)

    print("label:", description,'\nx:', coppelia_x, "\ny:",coppelia_y, "\nz:",coppelia_z,"\n")
    # Publish to ROS2
    # msg = Float32MultiArray()
    # msg.data = [coppelia_x, coppelia_y, coppelia_z]
    # publisher.publish(msg)

    return jsonify({'status': 'success', 'coordinates': [coppelia_x, coppelia_y, coppelia_z]}), 200

def convert_to_coppeliasim(x, y, z):
    # Adjust the coordinate system to match CoppeliaSim
    return x, -z, y  # Example conversion (depends on CoppeliaSim's coordinate system)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
# 修改代码以接受手机热点网段的数据
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)